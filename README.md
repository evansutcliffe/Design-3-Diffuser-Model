# Design-3-Diffuser-Model
Numerical modelling of optical diffuser

### Introduction

In photolithography a silicon wafer has a pattern etched onto it using a mask and UV-LED light. 
previous devices have used a ellipsoidal mirrors and collimating lenses to produce a parallel source of light however it was 
theorised that it would be cheaper to use LEDs as a distrusted light source. Modelling was done to test the uniformity of the light with and without an optical diffuser. Furthermore, tests were done to find the ideal distance between the light source and the wafer to increase uniformity.

### Technique

In this project light was modelled using a Monte Carlo simulation where light rays were discrete particles. These partials are sourced from the LED location which was modelled as a square grid. Partials are assigned an initial deflection angle which is normally distributed with the standard deviation approximated from the LED datasheet [1]. When interacting with the diffuser the partials are redirected by an angle taken from the a normal distribution from the diffuser data sheet[2]. For when the particle strikes the wafer the *X*-*Y* coordinates, and the angle were recorded. Transmission losses for the diffuser were neglected as only the variation of the light is being measured.

### Results

For testing the variance of light with the distance between the LEDs and the model was repeated for distances from 5-100mm. This was modelled without a diffuser and only used the variance in the *X* dimension as the model was assumed to be fully symmetrical. This found that the light which was most uniform (lowest variation) was at around 35mm. This verifies the experimental data from other sources which found similar results[3]. Further tests were done where the distance between the diffuser and LEDs. It was found that to minimise variance this distance should be reduced. 

![Figure 1](https://github.com/evansutcliffe/Design-3-Diffuser-Model/blob/master/distance%20calc.png)

*Figure 1, Figure 1 shows the variance of the light with distance between the diffuser and the wafer* 

The model was used to find the variance in the *X*-*Y* axis. In this model each LED produced 1000 light rays, and these were then binned and plotted in a 2D histogram. Figure 3 and 4 show the variation with and without a diffuser present. As can be seen, the light forms a regular pattern without the diffusers but with the diffuser variation is dominated by random noise. The Red circle in both images shows the area of interest as this is the maximum size of the wafer. As it can be seen the edge region of the image has a reduced intensity however due to this they can be discarded in the variation calculation. 

![Figure 2](https://github.com/evansutcliffe/Design-3-Diffuser-Model/blob/master/no_diffuser_circle.png)
*Figure 2, Figure 3 shows the regular pattern of light intensity due to the layout of the LED grid* 

![Figure 3](https://github.com/evansutcliffe/Design-3-Diffuser-Model/blob/master/diffuser_circle.png)
*Figure 3, Figure 3 shows the random variance of the light due to the diffuser plate* 

### Conclusion
The model provides a powerful method for validating the uniformity of the light and builds on the hypothesis that a diffuser would be needed to provide a uniform light source. Furthermore, it shows that reducing the distance between the diffuser and LED is beneficial. This suggests that wider angle LEDs would also reduce the variation of light intensity.


### bibliography

[1] https://uk.rs-online.com/web/p/uv-leds/1699814/

[2] https://www.thorlabs.com/thorproduct.cfm?partnumber=DG100X100-120

[3] UV-LED exposure system for low-cost photolithography https://www.researchgate.net/publication/262953366_UV-LED_exposure_system_for_low-cost_photolithography
