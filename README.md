# Design-3-Diffuser-Model
Ray Tracing model for of an optical diffuser for photolithography

### Introduction

In photolithography a silicon wafer has a pattern etched onto it using a optical mask and UV light source. 
Previous devices have used a ellipsoidal mirrors and collimating lenses to produce a parallel source of light. However, it was theorised that it would be cheaper to use a distributed light source such as an array of LEDs. Modelling was done to test the uniformity of the light with and without an optical diffuser with the aim of having the most uniform light intensity over the wafer. Furthermore, tests were done to find the ideal distance between the light source and the wafer.

### Technique

The project used a form of ray tracing where light rays were modelled as discrete particles. These partials were sourced from the LED locations. Partials are assigned an initial deflection angle from a normal distribution with the standard deviation and mean taken from the LED datasheet [1]. When interacting with the diffuser the partials are redirected by a random angle taken from a normal distribution based on the diffuser data sheet[2]. The output results were the *xy* coordinates and the angle of the light particles. Due to the size of the model assumptions can be made about the underlying distribution of the continuous light source from the discrete particle locations. Transmission losses for the diffuser were neglected as only the variation was relevant.

### 2D model results 

The model was used to find the uniformity in the *xy* plane. The light rays were sourced from the
LEDs and their location on the wafer was recorded. For these plots approximately 2.5×10<sup>7</sup> data
points were binned and plotted in a 2D histogram. Figure 1 shows the spread on a wafer at 10mm
displacement. As can be seen, the light forms a regular intensity pattern. The red circle shows the
area of interest as this is the diameter of the largest wafer. At this distance the model was tested
with a diffuser and improved the uniformity from 83% to 43%

![Figure 1](https://github.com/evansutcliffe/Design-3-Diffuser-Model/blob/master/ES10!D.png)
*Figure 1, 2D Light Intensity Plot.* 

Figure 2 is a repeat of the simulation but with the wafer placed 50mm from the LED UV source. The
system shows only random noise due to the simulation model and an underlying uniform distribution.
The edge region of the image has a reduced intensity due to the scattering of light to outside the
area plotted. However, as this is outside the area of interest it is not significant. It was found that a diffuser had a small negative impact on the uniformity at this distance. It was theorised that this
is due to the increased distribution range increasing the boundary effect and reducing the intensity
at the edge of the area of interest. Therefore, it was decided to not use a diffuser.

![Figure 2](https://github.com/evansutcliffe/Design-3-Diffuser-Model/blob/master/ES50!D.png)
*Figure 2, 2D Light Intensity Plot (note Figure 1 and Figure 2 use different scales).*

### Effect of Dispalcement 

A test of uniformity against displacement to the wafer was Condcuted. The percentage uniformity
was not used as it is sensitive to the data size which decreases with distance. It was first considered
to use the Kolmogorov-Smirnov test for uniformity, however it was found that as the dataset was
so large, any variation from a perfectly uniform distribution resulted in a negative result.
Instead the coefficient of variance (*Cv*) of the bins was used as in this situation it normalises for data
size. *Cv* is the ratio of the standard deviation σ and the mean μ as shown in Equation 1.

*Cv= σ/μ  (1)*

The simulation was repeated for distances between 5−150mm as can be seen in Figure 3 in blue.
Only data in the x dimension was used as the model was expected to be fully symmetrical. For
distances greater than 1m the light increased uniformity with displacements. For small displacements,
a local minimum was found at 22mm. This verifies the experimental data from other sources which
found similar results experimentally [3]. This is the point where the light from adjacent LEDs
interferes fully.

![Figure 3](https://github.com/evansutcliffe/Design-3-Diffuser-Model/blob/master/ESCv.png)
*Figure 3, Normalised Coefficient of Variance against Distance.*


As the uniformity of the model is worse at on the edge regions, *Cv* was also found from a subset of
the area of interest as shown in green. This showed a lower *Cv* value further away from the
local minimum.

### Conclusion
The model provides a powerful method for validating the uniformity of the light and builds on the hypothesis that a diffuser would be needed to provide a uniform light source. Furthermore, it shows that reducing the distance between the diffuser and LED is beneficial. This suggests that wider angle LEDs would also reduce the variation of light intensity.


### bibliography

[1] https://uk.rs-online.com/web/p/uv-leds/1699814/

[2] https://www.thorlabs.com/thorproduct.cfm?partnumber=DG100X100-120

[3] UV-LED exposure system for low-cost photolithography https://www.researchgate.net/publication/262953366_UV-LED_exposure_system_for_low-cost_photolithography
