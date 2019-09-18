# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 17:08:35 2019

@author: evans
"""
from myconfig import*
import numpy as np

def intensity(data):
    midpoint_x=width/2
    midpoint_y=length/2 
    data = data[((data[:,0]-midpoint_x)*(data[:,0]-midpoint_x)+(data[:,1]-midpoint_y)*(data[:,1]-midpoint_y)<(waferR*waferR))]
    if(use_diffuser):
        losses=transmission
    else:
        losses=1   
    light_ray_intensity = (LED_intensity/rep)*data.shape[0]*losses/(np.pi*(7.62*7.62)) 
    print(light_ray_intensity,'mw/cm^2')
    return data