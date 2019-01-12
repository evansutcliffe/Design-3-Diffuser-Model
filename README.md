# Design-3-Diffuser-Model
Numerical modelling of optical diffuser

### Introduction

In photolithography a silicon wafer has a pattern etched onto it using a optical mask and UV light source. 
previous devices have used a ellipsoidal mirrors and collimating lenses to produce a parallel source of light however it was 
theorised that it would be cheaper to use a distributed light source such as an array of LEDs. Modelling was done to test the uniformity of the light with and without an optical diffuser with the aim of having the most uniform light intensity over the wafer. Furthermore, tests were done to find the ideal distance between the light source and the wafer.

### Technique

In this project light was modelled using a Monte Carlo simulation where light rays were discrete particles. These partials are sourced from the LED locations. Partials are assigned an initial deflection angle from a normal distribution with the standard deviation and mean taken from the LED datasheet [1]. When interacting with the diffuser the partials are redirected by a random angle taken from a normal distribution based on the diffuser data sheet[2]. The output results were the *X*-*Y* coordinates and the angle of the light particles. Due to the size of the model assumptions can be made about the underlying distribution of the continuous light source from the discrete particle locations. Transmission losses for the diffuser were neglected as only the variation was relevant.

### Results

For testing the variance of light with the distance the simulation was repeat for distances between the LEDs and the wafer of 5-100mm. This was modelled without a diffuser and only used the variance in the *X* dimension as the model was assumed to be fully symmetrical. This found that the light which was most uniform (lowest variation) was at around 35mm. This verifies the experimental data from other sources which found similar results[3]. Further tests were done where the distance between the diffuser and LEDs. It was found that to minimise variance this distance should be reduced. 

![Figure 1](https://github.com/evansutcliffe/Design-3-Diffuser-Model/blob/master/distance%20calc.png)

*Figure 1, Figure 1 shows the variance of the light with distance between the diffuser and the wafer* 

The model was used to find the variance in the *X*-*Y* axis. In this model each LED produced 1000 light rays, and these were then binned and plotted in a 2D histogram. Figure 2 shows the variation without a diffuser present. As can be seen, the light forms a regular pattern without the diffusers but with the diffuser variation is dominated by random noise. The Red circle in both images shows the area of interest as this is the maximum size of the wafer. As it can be seen the edge region of the image has a reduced intensity however due to this, they can be discarded in the variation calculation. The distribution of the angle of the light rays is shown on the right hand side of the figure. Figure 3 is a repeat of the simulation but with a diffuser placed 5mm from the LED light source. In this model random noise dominates the distribution of the light and is more uniform This shows that for both systems there is a significant range of light angle. 

Finally, the light intensity on the wafer was found. The calculations show that with 256 LEDs the intensity is 16.2 mw/cm<sup>2 . This means that this setup can meet the specification for light intensity without the use of a focusing lens
![Figure 2](https://github.com/evansutcliffe/Design-3-Diffuser-Model/blob/master/no%20diffuser.png)
*Figure 2, Figure 2 shows the regular pattern of light intensity due to the layout of the LED grid* 

![Figure 3](https://github.com/evansutcliffe/Design-3-Diffuser-Model/blob/master/diffuser.png)
*Figure 3, Figure 3 shows the random variance of the light due to the diffuser plate* 

### Conclusion
The model provides a powerful method for validating the uniformity of the light and builds on the hypothesis that a diffuser would be needed to provide a uniform light source. Furthermore, it shows that reducing the distance between the diffuser and LED is beneficial. This suggests that wider angle LEDs would also reduce the variation of light intensity.


### bibliography

[1] https://uk.rs-online.com/web/p/uv-leds/1699814/

[2] https://www.thorlabs.com/thorproduct.cfm?partnumber=DG100X100-120

[3] UV-LED exposure system for low-cost photolithography https://www.researchgate.net/publication/262953366_UV-LED_exposure_system_for_low-cost_photolithography
