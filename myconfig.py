# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 17:15:00 2019

@author: evans
"""



## variables you can change 
LightW,LightL= 178, 178 # size of lightsource 
width,length = 178, 178 # size of mask 
L = 1 # distance between LED and diffuser
height = 50 # distance between LEDs and wafer
LED_intensity = 40 #  mw per LED
transmission = 0.6 # diffuser transmission
LED_angle = 30 # angle of LED beam (assumed 2 sd) 
diffuser_angle = 30 # angle of diffuser (assumed 2 sd) 
max_angle_degrees=10 # degrees, max allowable optical angle





use_diffuser = 1
intensity = 0
use_angle_filter= 0# calculate the final intensity after using a optical angle filter
plot=1
##

## simulation parameters
rep =1000 # light rays per LED
nbins = 1000 # bins for 2d hist
histbin = 1000 #bins for angle hist
##

