# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 17:15:00 2019

@author: evans
"""



## variables you can change 
dim_x,dim_y=16,16
LED_count =dim_x*dim_y
LightW,LightL= 178, 178 # size of lightsource (mm) 
waferR = 76.2 # wafer radius in mm
width,length = 178, 178 # size of mask (mm)
L = 1 # distance between LED and diffuser (mm)
height = 50 # distance between LEDs and wafer (mm)
LED_intensity = 40 #  mw per LED
transmission = 0.6 # diffuser transmission index
LED_angle = 30 # angle of LED beam (assumed 2 standard deviations) 
diffuser_angle = 30 # angle of diffuser (assumed 2 standard deviations) 
max_angle_degrees=10 # degrees, max allowable optical angle for acceptable lithography

x_save=[]
y_save=[]
dx_save=[]
dy_save=[]




use_diffuser = 1 # calculate diffusion with a diffuser present
use_angle_filter= 0# calculate the final intensity after using a optical angle filter
##

## simulation parameters
rep =10000 # light rays sper LED
nbins = 1000 # bins for 2d hist
histbin = 1000 #bins for angle hist
##

def save_data(x,y,ax,ay):
    x_save=x
    y_save=y
    dx_save=ax
    dy_save=ay
