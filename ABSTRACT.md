The **PH2: A Dermoscopic Image Database for Research and Benchmarking** dataset was developed for computer-aided diagnosis systems, specifically for the classification of dermoscopic images of melanoma. Its purpose is to facilitate comparative studies involving segmentation and classification algorithms. This dataset comprises a total of 200 dermoscopic images of melanocytic lesions with a vast amount of metainformation. It includes 80 common nevi, 80 atypical nevi, and 40 melanomas.

Within the PH² database, each image comes with medical annotations. These annotations include the medical segmentation of the *lesion*, clinical and histological diagnoses, and the evaluation of various dermoscopic criteria, such as colors, pigment network, dots/globules, streaks, regression areas, and blue-whitish veil. The dermoscopic images were captured at the Dermatology Service of Hospital Pedro Hispano in Matosinhos, Portugal. These images were consistently acquired under the same conditions using the Tuebinger Mole Analyzer system, with a magnification of 20x. They are 8-bit RGB color images with a resolution of 768x560 pixels.

The assessment of each parameter was performed by an expert dermatologist, according to the following parameters:

<div>
  <table border="1" bordercolor="#CCCCCC" cellpadding="2" style="margin-top:15px; margin-bottom:5px;">
    <tbody>
      <tr align="center" bgcolor="#CCCCCC">
        <td><strong>Criterion</strong></td>
        <td><strong>PH² Segmentation</strong></td>
      </tr>

  <tr>
    <td rowspan="3"><strong>Clinical Diagnosis</td>
    <td>0 - Common Nevus</td>
  </tr>
  <tr>
    <td>1 - Atypical Nevus</td>
  </tr>
  <tr>
    <td>2 - Melanoma</td>
  </tr

  <tr>
    <td rowspan="1"><strong>Lesion Segmentation</td>
    <td>Available as a binary mask (with the samsize of the original image).</td>
  </tr

  <tr>
    <td rowspan="1"><strong>Color Segmentation</td>
    <td>Available as a binary mask (with the samsize of the original image) (If available).</td>
  </tr

  <tr>
    <td rowspan="3"><strong>Asymmetry</strong></td>
    <td>0 - Fully Symmetry</td>
  </tr>
  <tr>
    <td>1 – Asymmetry in One Axis</td>
  </tr>
  <tr>
    <td>2 - Fully Asymmetry</td>
  </tr

  <tr>
    <td rowspan="2"><strong>Pigment Networkstrong</td>
    <td>AT - Atypical</td>
  </tr>
  <tr>
    <td>T - Typical</td>
  </tr

  <tr>
    <td rowspan="3"><strong>Dots/Globules</strong>
    <td>A - Absent</td>
  </tr>
  <tr>
    <td>AT - Atypical</td>
  </tr>
  <tr>
    <td>T - Typical</td>
  </tr
  
  <tr>
    <td rowspan="2"><strong>Streaks</strong></td>
    <td>A - Absent</td>
  </tr>
  <tr>
    <td>P - Present</td>
  </tr

  <tr>
    <td rowspan="2"><strong>Regression Areasstrong</td>
    <td>A - Absent</td>
  </tr>
  <tr>
    <td>P - Present</td>
  </tr

  <tr>
    <td rowspan="2"><strong>Blue Whitish Veilstrong</td>
    <td>A - Absent</td>
  </tr>
  <tr>
    <td>P - Present</td>
  </tr

  <tr>
    <td rowspan="6"><strong>Colors</strong></td>
    <td>1 - White</td>
  </tr>
  <tr>
    <td>2 - Red</td>
  </tr>
  <tr>
    <td>3 - Light-Brown</td>
  </tr>
  <tr>
    <td>4 - Dark-Brown</td>
  </tr>
  <tr>
    <td>5 - Blue-Gray</td>
  </tr>
  <tr>
    <td>6 - Black</td>
  </tr>
    </tbody>
  </table>
</div>

The rather small number of melanomas, compared with the other two types of melanocytic lesions, can be explained by two main reasons. First of all, the number of real cases of melanomas is actually much smaller than the other ones. In addition, as melanomas are usually not completely inserted in the image frame and present many image artifacts, they are not always suitable to be used as ground truth in the evaluation of CAD systems.

For each image in the database, the manual segmentation and the clinical diagnosis of the skin lesion as well as theidentiﬁcation of other important dermoscopic criteria are available. These dermoscopic criteria include the assessment of the lesion asymmetry, and also the identiﬁcation of colors in several differential structures, such as pigment network, dots, globules, streaks, regression areas, and blue-whitish veil.

The size of the PH² database (200 images) might seem small, particularly when compared with a traditional machine learning ground truth database, which may have hundreds of or thousands of annotated images. However, it is important to highlight that the annotation of dermoscopic images is not just a binary issue (benign or malign). The annotation of each image requires a large amount of time and effort since several dermoscopic features have to be assessed to perform the lesion diagnosis. Moreover, the skin lesion and the color classes present in each image have to be manually segmented by expert clinicians. Besides benchmarking computer vision/machine learning algorithms, a database like PH² can be also used for medical training. For instance, dermatologist trainees can test their skills by comparing their own diagnosis and evaluation with the ground truth available in the PH² database.

This image database contains a total of 200 dermoscopic images, containing 80 common nevi, 80 atypical nevi, and 40 melanomas. All dermoscopic images are either from the skin type II or III, according to the [Fitzpatrick skintype classiﬁcation scale](https://www.bioline.org.br/request?dv09029). Therefore, the skin colors represented in the PH² database may vary from white to cream white. As illustrated in Fig.1, the images of the database were carefully selected taking into account their quality, resolution, and dermoscopic features. Every image is evaluated by an expert dermatologist with regard to the following parameters:

- Manual segmentation of the skin lesion
- Clinical and histological (when available) diagnosis
- Dermoscopic criteria (Asymmetry; Colors; Pigment net-work; Dots/Globules; Streaks; Regression areas; Blue-whitish veil)

![Fig. 1: An illustrative collection of images from PH² database, including common nevi (1st row), atypical nevi(2nd row) and melanomas (3rd row)](https://i.ibb.co/bv9QBkt/2023-09-24-150038.png)

<span style="font-size: smaller; font-style: italic;">Fig. 1: An illustrative collection of images from PH² database, including common nevi (1st row), atypical nevi(2nd row) and melanomas (3rd row)</span>

Dermatologists performed the manual segmentation and annotation of the images using a customized annotation tool for dermoscopic images, called [DerMAT](https://dl.acm.org/doi/10.1145/2304496.2304501). As an example, Fig.2 shows the manual segmentation and annotation of two regions of interest using the DerMAT software.

![Fig2](https://i.ibb.co/G5M9KkC/Manual-segmentation-of-three-melanocytic-lesions-common-nevus-left-atypical-nevus.jpg)

<span style="font-size: smaller; font-style: italic;">Fig. 2: DerMAT interface for the segmentation and labeling of multiple regions of interest.</span>

## Manual segmentation of the skin lesion

The manual segmentation of the skin lesion, performed by expert dermatologists, is essential information for the evaluation of the segmentation step of a CAD system. In this database, the manual segmentation of each image is available as a binary mask, in which pixels with an intensity value of 1 correspond to the segmented lesion, while pixels with a value of 0 correspond to the background. This binary mask has the same size as the original image and, hence, it can be easily used to extract the boundary coordinates of the lesion. Figure 3 presents examples of three dermoscopic images and the corresponding ground truth (manual) segmentations.

![Fig3](https://i.ibb.co/CHTd5Jv/Original-image-left-blue-gray-middle-and-dark-brown-region-right.png)

<span style="font-size: smaller; font-style: italic;">Fig. 3: Manual segmentation of three melanocytic lesions: common nevus (left), atypical nevus (middle), and melanoma(right).</span>

## Clinical diagnosis

The melanocytic lesions can be divided into two main groups concerning their nature: benign lesions (which include common and atypical nevus) and malignant lesions(or melanomas). Therefore, each image of the database isclassiﬁed into common nevus, atypical nevus, or melanoma (Fig.3). The histological diagnosis is only available for some of the images since the histological test is performed for those lesions considered highly suspicious by dermatologists.

## Dermoscopic criteria

The set of dermoscopic features that is available in the PH² database corresponds to those features that the dermatologist of Hospital Pedro Hispano considers more relevant to performing a clinical diagnosis. 
