# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 17:08:35 2019

@author: evans
"""
from myconfig import*
import numpy as np

def intensity(x,y,ax,ay):
    midpoint_x=LightL/2
    midpoint_y=LightW/2
    square=waferR/np.sqrt(2)
    cir = [(midpoint_x-waferR),(midpoint_x+waferR),(midpoint_y-waferR),(midpoint_y+waferR)]
    #sqr = [(midpoint_x-square),(midpoint_x+square),(midpoint_y-square),(midpoint_y+square)]
    ray_count=0
    for (x1,y1,ax1,ay1) in zip(x,y,ax,ay):
        if(x1<cir[0] or y1<cir[2] or x1>cir[1] or y1>cir[3]):
            pass
        #elif(x>sqr[0] and y>sqr[2] and x<sqr[1] and y<sqr[3]):
         #   ray_count=ray_count+1
        elif ((x1-midpoint_x)*(x1-midpoint_x)+(y1-midpoint_y)*(y1-midpoint_y)<(waferR*waferR)):
            ray_count=ray_count+1

    if(use_diffuser):
        losses=transmission
    else:
        losses=1      
    light_ray_intensity = (LED_intensity/rep)*ray_count*losses/(np.pi*(7.62*7.62)) 
    print(light_ray_intensity,'mw/cm^2')