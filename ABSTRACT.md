The increasing incidence of melanoma has recently promoted the development of computer-aided diagnosis systems for the classification of dermoscopic images. The PH² dataset has been developed for research and benchmarking purposes, in order to facilitate comparative studies on both segmentation and classification algorithms of dermoscopic images. **PH²** is a dermoscopic image database acquired at the Dermatology Service of Hospital Pedro Hispano, Matosinhos, Portugal.

The dermoscopic images were obtained at the Dermatology Service of Hospital Pedro Hispano (Matosinhos, Portugal) under the same conditions through Tuebinger Mole Analyzer system using a magnification of 20x. They are 8-bit RGB color images with a resolution of 768x560 pixels.

This image database contains a total of 200 dermoscopic images of melanocytic lesions, including 80 common nevi, 80 atypical nevi, and 40 melanomas. The PH² database includes medical annotation of all the images namely medical segmentation of the lesion, clinical and histological diagnosis and the assessment of several dermoscopic criteria (colors; pigment network; dots/globules; streaks; regression areas; blue-whitish veil).

The assessment of each parameter was performed by an expert dermatologist, according to the following parameters:

<div>
  <table border="1" bordercolor="#CCCCCC" cellpadding="2" style="margin-top:15px; margin-bottom:5px; font-size:10px">
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

The rather small number of melanomas,compared with the other two types of melanocytic lesions,can be explained by two main reasons. First of all, thenumber of real cases of melanomas is actually much smallerthan the other ones. In addition, as melanomas are usuallynot completely inserted in the image frame and present manyimage artifacts, they are not always suitable to be used asground truth in the evaluation of CAD systems.

For each image in the database, the manual segmentationand the clinical diagnosis of the skin lesion as well as theidentiﬁcation of other important dermoscopic criteria areavailable. These dermoscopic criteria include the assessmentof the lesion asymmetry, and also the identiﬁcation of colorsand several differential structures, such as pigment network,dots, globules, streaks, regression areas and blue-whitish veil.The PH² will be made freely available (online) si-multaneously with the EMBC 2013 conference. 

The size of the PH² database (200 images) might seemssmall, particularly when compared with a traditional machinelearning ground truth database, which may have hundreds orthousands of annotated images. However, it is important tohighlight that the annotation of dermoscopic images is notjust a binary issue (benign or malign). The annotation ofeach image requires a large amount of time and effort, sinceseveral dermoscopic features have to be assessed to performthe lesion diagnosis. Moreover, the skin lesion and the colorclasses present in each image have to be manually segmented by expert clinicians.Besides benchmarking of computer vision/machine learn-ing algorithms, a database like PH2can be also used formedical training. For instance, dermatologist trainees can testtheir skills by comparing their own diagnosis and evaluationwith the ground truth available in the PH² database.

The PH² database was built up through a joint researchcollaboration between the Universidade do Porto, T´ecnicoLisboa, and the Dermatology service of Hospital PedroHispano in Matosinhos, Portugal. The dermoscopic imageswere obtained under the same conditions through TuebingerMole Analyzer system using a magniﬁcation of 20×. Theyare 8-bit RGB color images with a resolution of 768 × 560pixels.

This image database contains a total of 200 dermoscopicimages, containing 80 common nevi, 80 atypical nevi, and40 melanomas. All dermoscopic images are either fromthe skin type II or III, according to the [Fitzpatrick skintype classiﬁcation scale](https://www.bioline.org.br/request?dv09029). Therefore, the skin coloursrepresented in the PH2database may vary from white tocream white. As illustrated in Fig.1, the images of thedatabase were carefully selected taking into account theirquality, resolution and dermoscopic features. Every imagewas evaluated by an expert dermatologist with regard to thefollowing parameters:

- Manual segmentation of the skin lesion
- Clinical and histological (when available) diagnosis
- Dermoscopic criteria (Asymmetry; Colors; Pigment net-work; Dots/Globules; Streaks; Regression areas; Blue-whitish veil)

![Fig. 1: An illustrative collection of images from PH2database, including common nevi (1st row), atypical nevi(2nd row) and melanomas (3rd row)](https://i.ibb.co/bv9QBkt/2023-09-24-150038.png)

<i>Fig. 1: An illustrative collection of images from PH2database, including common nevi (1st row), atypical nevi(2nd row) and melanomas (3rd row)</i>

Dermatologists performed the manual segmentation and an-notation of the images using a customized annotation tool fordermoscopic images, called [DerMAT](https://dl.acm.org/doi/10.1145/2304496.2304501). As an example,Fig.2 shows the manual segmentation and annotation of tworegions of interest using the DerMAT software.

![Fig2](https://i.ibb.co/G5M9KkC/Manual-segmentation-of-three-melanocytic-lesions-common-nevus-left-atypical-nevus.jpg)

<i>Fig. 2: DerMAT interface for the segmentation and labelingof multiple regions of interest.</i>

## Manual segmentation of the skin lesion

The manual segmentation of the skin lesion, performedby expert dermatologists, is an essential information for theevaluation of the segmentation step of a CAD system.In this database, the manual segmentation of each imageis available as a binary mask, in which pixels with intensityvalue of 1 correspond to the segmented lesion, while pixelswith value 0 correspond to the background. This binary maskhas the same size of the original image and, hence, it can beeasily used to extract the boundary coordinates of the lesion.Figure 3 presents examples of three dermoscopic images andthe corresponding ground truth (manual) segmentations.

![Fig3](https://i.ibb.co/CHTd5Jv/Original-image-left-blue-gray-middle-and-dark-brown-region-right.png)

<i>Fig. 3: Manual segmentation of three melanocytic lesions:common nevus (left), atypical nevus (middle) and melanoma(right).</i>

## Clinical diagnosis

The melanocytic lesions can be divided in two maingroups concerning their nature: benign lesions (which in-clude common and atypical nevus) and malignant lesions(or melanomas). Therefore, each image of the database isclassiﬁed into common nevus, atypical nevus, or melanoma(Fig.3). The histological diagnosis is only available for someof the images, since the histological test is just performed forthose lesions considered highly suspicious by dermatologists

## Dermoscopic criteria

The set of dermoscopic features that is available in the PH2database corresponds to those features that the dematologistsof Hospital Pedro Hispano consider more relevant to performa clinical diagnosis. 
