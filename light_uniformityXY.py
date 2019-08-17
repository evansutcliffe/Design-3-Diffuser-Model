# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 11:36:22 2018

@author: evans
"""

import numpy as np 
import plot_data
import print_uniformity
import trace_rays
import light_ray_intensity
from myconfig import *

# top down view of intensity on a wafer
# input distance and other variables

cood_xy = np.mgrid[0:LightW:16j, 0:LightL:16j].reshape(2,-1).T #hardcoded for 16 x 16 LED grid
max_allowable_angle=(max_angle_degrees*np.pi/180) # degrees, max allowable optical angle

cood_diffuser =[]
cood_wafer =[]

if (use_diffuser):
    distance = L
    print("calcuating diffuser scatter")
else:
    distance = height 
    print("calcuating scatter")
  
    
wafer=trace_rays.trace_rays(cood_xy,distance)
light_ray_intensity.intensity(wafer)



x,y,thetax,thetay = zip(*wafer) 
x = np.array(x)
y = np.array(y)
ax = np.array(thetax)*180/np.pi
ay = np.array(thetay)*180/np.pi


print_uniformity.print_uniformity(x)
plot_data.plot_data(x,y,ax,ay,nbins,histbin)






  
  
  