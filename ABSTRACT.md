The increasing incidence of melanoma has recently promoted the development of computer-aided diagnosis systems for the classification of dermoscopic images. The PH² dataset has been developed for research and benchmarking purposes, in order to facilitate comparative studies on both segmentation and classification algorithms of dermoscopic images. **PH²** is a dermoscopic image database acquired at the Dermatology Service of Hospital Pedro Hispano, Matosinhos, Portugal.

The dermoscopic images were obtained at the Dermatology Service of Hospital Pedro Hispano (Matosinhos, Portugal) under the same conditions through Tuebinger Mole Analyzer system using a magnification of 20x. They are 8-bit RGB color images with a resolution of 768x560 pixels.

This image database contains a total of 200 dermoscopic images of melanocytic lesions, including 80 common nevi, 80 atypical nevi, and 40 melanomas. The PH² database includes medical annotation of all the images namely medical segmentation of the lesion, clinical and histological diagnosis and the assessment of several dermoscopic criteria (colors; pigment network; dots/globules; streaks; regression areas; blue-whitish veil).

The assessment of each parameter was performed by an expert dermatologist, according to the following parameters:

| Criterion           | PH² Segmentation                                                       |
|---------------------|------------------------------------------------------------------------|
| Clinical Diagnosis  | 0 - Common Nevus                                                       |
|                     | 1 - Atypical Nevus                                                     |
|                     | 2 - Melanoma                                                           |
| Lesion Segmentation | Available as a binary mask (with the same size of the original image). |
| Color Segmentation  | Available as a binary mask (If available).                             |
| Asymmetry           | 0 - Fully Symmetry                                                     |
|                     | 1 - Asymmetry in One Axis                                              |
|                     | 2 - Fully Asymmetry                                                    |
| Pigment Network     | AT - Atypical                                                          |
|                     | T - Typical                                                            |
| Dots/Globules       | A - Absent                                                             |
|                     | AT - Atypical                                                          |
|                     | T - Typical                                                            |
| Streaks             | A - Absent                                                             |
|                     | P - Present                                                            |
| Regression Areas    | A - Absent                                                             |
|                     | P - Present                                                            |
| Blue Whitish Veil   | A - Absent                                                             |
|                     | P - Present                                                            |
| Colors              | 1 - White                                                              |
|                     | 2 - Red                                                                |
|                     | 3 - Light-Brown                                                        |
|                     | 4 - Dark-Brown                                                         |
|                     | 5 - Blue-Gray                                                          |
|                     | 6 - Black                                                              |
