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
