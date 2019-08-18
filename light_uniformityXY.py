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
import myconfig
import time



# top down view of intensity on a wafer
# input distance and other variables in config file

t0 = time.clock()

LED_Grid = np.mgrid[0:LightW:dim_x*1j, 0:LightL:dim_y*1j].reshape(2,-1).T # e.g. 16 x 16 LED grid
LED_Grid=LED_Grid
t1=time.clock()

(x,y,ax,ay)=trace_rays.trace_rays(LED_Grid,L,height)
#myconfig.save_data(x,y,ax,ay)
t2 = time.clock()
print("calcuating light wafer intensity (for diffuser)")
print("")
light_ray_intensity.intensity(x,y,ax,ay)   


t3 = time.clock()
x , y = np.array(x), np.array(y)
ax,ay  = np.array(ax)*180/np.pi, np.array(ay)*180/np.pi

print_uniformity.print_uniformity(x)

t4 = time.clock()
print("plotting graphs")
print("")
plot_data.plot_data(x,y,ax,ay)

t5 = time.clock()


print("setup:"+str((t1-t0)*1000)+"ms")
print("calc rays:"+str((t2-t1)*1000)+"ms")
print("calc intensitiy:"+str((t3-t2)*1000)+"ms")
print("calc statistics:"+str((t4-t3)*1000)+"ms")
print("plot:"+str((t5-t4)*1000)+"ms")






  
  
  