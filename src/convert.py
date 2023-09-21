import supervisely as sly
import os, glob
from dataset_tools.convert import unpack_if_archive
import src.settings as s
from urllib.parse import unquote, urlparse
from supervisely.io.fs import get_file_name, get_file_name_with_ext
import shutil

from tqdm import tqdm

def download_dataset(teamfiles_dir: str) -> str:
    """Use it for large datasets to convert them on the instance"""
    api = sly.Api.from_env()
    team_id = sly.env.team_id()
    storage_dir = sly.app.get_data_dir()

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, str):
        parsed_url = urlparse(s.DOWNLOAD_ORIGINAL_URL)
        file_name_with_ext = os.path.basename(parsed_url.path)
        file_name_with_ext = unquote(file_name_with_ext)

        sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
        local_path = os.path.join(storage_dir, file_name_with_ext)
        teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

        fsize = api.file.get_directory_size(team_id, teamfiles_dir)
        with tqdm(
            desc=f"Downloading '{file_name_with_ext}' to buffer...",
            total=fsize,
            unit="B",
            unit_scale=True,
        ) as pbar:        
            api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)
        dataset_path = unpack_if_archive(local_path)

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, dict):
        for file_name_with_ext, url in s.DOWNLOAD_ORIGINAL_URL.items():
            local_path = os.path.join(storage_dir, file_name_with_ext)
            teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

            if not os.path.exists(get_file_name(local_path)):
                fsize = api.file.get_directory_size(team_id, teamfiles_dir)
                with tqdm(
                    desc=f"Downloading '{file_name_with_ext}' to buffer...",
                    total=fsize,
                    unit="B",
                    unit_scale=True,
                ) as pbar:
                    api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)

                sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
                unpack_if_archive(local_path)
            else:
                sly.logger.info(
                    f"Archive '{file_name_with_ext}' was already unpacked to '{os.path.join(storage_dir, get_file_name(file_name_with_ext))}'. Skipping..."
                )

        dataset_path = storage_dir
    return dataset_path
    
def count_files(path, extension):
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                count += 1
    return count
    
def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    ### Function should read local dataset and upload it to Supervisely project, then return project info.###
    images_path = os.path.join("PH2Dataset","PH2 Dataset images")
    tags_path = os.path.join("PH2Dataset","PH2_dataset.txt")
    ds_name = "ds"
    mask_folder_suffix = "_lesion"
    mask_ext = "_lesion.bmp"
    batch_size = 30


    def create_ann(image_path):
        labels = []
        tags = []

        image_name = get_file_name(image_path)

        tags_data = image_to_tags[image_name]
        if len(tags_data[0]) > 0:
            histological_value = tags_data[0]
            tag_histological = sly.Tag(histological_diagnosis, value=histological_value)
            tags.append(tag_histological)

        clinical_value = legends_clinical[tags_data[1]]
        tag_clinical = sly.Tag(clinical_diagnosis, value=clinical_value)
        asymmetry_value = legends_asymmetry[tags_data[2]]
        tag_asymmetry = sly.Tag(asymmetry, value=asymmetry_value)
        pigment_value = over_legends[tags_data[3]]
        tag_pigment = sly.Tag(pigment_network, value=pigment_value)
        dots_value = over_legends[tags_data[4]]
        tag_dots = sly.Tag(dots, value=dots_value)
        streaks_value = over_legends[tags_data[5]]
        tag_streaks = sly.Tag(streaks, value=streaks_value)
        regression_value = over_legends[tags_data[6]]
        tag_regression = sly.Tag(regression_areas, value=regression_value)
        veil_value = over_legends[tags_data[7]]
        tag_veil = sly.Tag(veil, value=veil_value)
        colors = []
        color_values = tags_data[8]
        for curr_color in color_values:
            colors.append(colors_legends[curr_color])
        colors_value = ", ".join(colors)
        tag_color = sly.Tag(legends_colors, value=colors_value)

        tags.extend(
            [
                tag_clinical,
                tag_asymmetry,
                tag_pigment,
                tag_dots,
                tag_streaks,
                tag_regression,
                tag_veil,
                tag_color,
            ]
        )

        subfolder = image_name + mask_folder_suffix
        mask_path = os.path.join(images_path, image_name, subfolder, image_name + mask_ext)

        mask_np = sly.imaging.image.read(mask_path)[:, :, 0]
        img_height = mask_np.shape[0]
        img_wight = mask_np.shape[1]

        mask = mask_np == 255
        curr_bitmap = sly.Bitmap(mask)
        curr_label = sly.Label(curr_bitmap, obj_class)
        labels.append(curr_label)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels, img_tags=tags)


    image_to_tags = {}
    with open(tags_path) as f:
        content = f.read().split("\n")
        for idx, curr_data in enumerate(content):
            if idx > 0 and idx < 201:
                curr_data = curr_data.replace(" ", "").split("||")[1:-1]
                data_3 = curr_data[3].split("|")
                curr_data[3] = data_3
                image_to_tags[curr_data[0]] = sum(
                    [[curr_data[1]], [curr_data[2]], curr_data[3], [curr_data[4]]], []
                )

    obj_class = sly.ObjClass("lesion", sly.Bitmap)

    histological_diagnosis = sly.TagMeta("histological_diagnosis", sly.TagValueType.ANY_STRING)
    clinical_diagnosis = sly.TagMeta("clinical_diagnosis", sly.TagValueType.ANY_STRING)
    asymmetry = sly.TagMeta("asymmetry", sly.TagValueType.ANY_STRING)
    pigment_network = sly.TagMeta("pigment_network", sly.TagValueType.ANY_STRING)
    dots = sly.TagMeta("dots/globules", sly.TagValueType.ANY_STRING)
    streaks = sly.TagMeta("streaks", sly.TagValueType.ANY_STRING)
    regression_areas = sly.TagMeta("regression_areas", sly.TagValueType.ANY_STRING)
    veil = sly.TagMeta("blue-whitish_veil", sly.TagValueType.ANY_STRING)
    legends_colors = sly.TagMeta("colors", sly.TagValueType.ANY_STRING)


    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(
        obj_classes=[obj_class],
        tag_metas=[
            histological_diagnosis,
            clinical_diagnosis,
            asymmetry,
            pigment_network,
            dots,
            streaks,
            regression_areas,
            veil,
            legends_colors,
        ],
    )
    api.project.update_meta(project.id, meta.to_json())

    legends_clinical = {"0": "Common Nevus", "1": "Atypical Nevus", "2": "Melanoma"}
    legends_asymmetry = {"0": "Fully Symmetric", "1": "Symetric in 1 axe", "2": "Fully Asymmetric"}
    over_legends = {"A": "Absent", "AT": "Atypical", "P": "Present", "T": "Typical"}
    colors_legends = {
        "1": "white",
        "2": "red",
        "3": "light brown",
        "4": "dark brown",
        "5": "blue gray",
        "6": "black",
    }

    all_images_pathes = glob.glob(images_path + "/*/*/*.bmp")
    images_pathes = [im_path for im_path in all_images_pathes if len(get_file_name(im_path)) == 6]

    dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

    progress = sly.Progress("Create dataset {}".format(ds_name), len(images_pathes))

    for img_pathes_batch in sly.batched(images_pathes, batch_size=batch_size):
        img_names_batch = [get_file_name_with_ext(im_path) for im_path in img_pathes_batch]

        img_infos = api.image.upload_paths(dataset.id, img_names_batch, img_pathes_batch)
        img_ids = [im_info.id for im_info in img_infos]

        anns = [create_ann(image_path) for image_path in img_pathes_batch]
        api.annotation.upload_anns(img_ids, anns)

        progress.iters_done_report(len(img_names_batch))

    return project
