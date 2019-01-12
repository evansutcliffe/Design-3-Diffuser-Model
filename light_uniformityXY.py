# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 11:36:22 2018

@author: evans
"""

import numpy as np 
import matplotlib.pyplot as plt

 



## variables you can change 
x= 256 # number of LEDs # hard coded for 16 by 16
spaceing = np.round(np.sqrt(x)) # unused 
LightW,LightL= 178, 178 # size of lightsource 
width,length = 178, 178 # size of mask 
L = 5 # distance between mask and diffuser
height = 35 # distance between LEDs and wafer
LED_intensity = 40 #  mw per LED
transmission = 0.6 # diffuser transmission
LED_angle = 30 # angle of LED beam (assumed 2 sd) 
diffuser_angle = 30 # angle of diffuser (assumed 2 sd) 
max_allowable_angle=10 # degrees, max allowable optical angle
use_diffuser = 1
intensity = 1
use_angle_filter=0 # calculate the final intensity after using a optical angle filter
##

## simulation parameters
rep =1000 # light rays per LED
nbins = 100 # bins for charts
histbin = 100 #bins for histogram
##


cood_xy = np.mgrid[0:LightW:16j, 0:LightL:16j].reshape(2,-1).T #hardcoded for 16 x 16
cood_diffuser =[]
cood_wafer =[]
angle =[]



if (use_diffuser):
    distance = height
    print("calcuating diffuser scatter")
else:
    distance = L
    print("calcuating light wafer intensity")
  
    
mu, sigma = 0, LED_angle/2*(np.pi/180) # mean and standard deviation
for LED in cood_xy:
    x,y = LED[0],LED[1] # xy coordinates in a topdown view
    thetax = np.random.normal(mu, sigma, rep)
    x = x + distance*(np.tan(thetax))
    thetay = np.random.normal(mu, sigma, rep)
    y =y + distance*(np.tan(thetay))
    for i in range(rep):
        if (x[i]>0 and x[i] < length and (y[i]>0 and y[i] < width)):
            cood_diffuser.append((x[i],y[i],thetax[i],thetay[i])) 
            a = np.sqrt((thetay[i])*(thetay[i])+(thetax[i])*(thetax[i]))
            angle.append(a*180/np.pi)
            # if light ray outside of diffuser/wafer boundary then disgard
            
            
if (use_diffuser):
    print("calcuating light wafer intensity (for diffuser)")
    angle=[]
    distance = height - L;     
    mu, sigma = 0, diffuser_angle/2*(np.pi/180) # assumed normal distribution of light?
    random_theta = np.random.normal(mu, sigma, len(cood_diffuser)*2) # random values for x,y
    for i in range(len(cood_diffuser)):
        (x, y, thetax,thetay), dtx, dty  = cood_diffuser[i], random_theta[i], random_theta[i+len(cood_diffuser)]
        x = x + distance*(np.tan(thetax+dtx))
        y = y + distance*(np.tan(thetay+dty))
        a = np.sqrt((thetay+dty)*(thetay+dty)+(thetax+dtx)*(thetax+dtx))
        if (x>0 and x < length and (y>0 and y < width)):
            cood_wafer.append((x,y))
            angle.append(a*180/np.pi)

if (intensity):
    light_ray_list=[]
    for x,y in cood_wafer:
        if ((x-89)*(x-89)+(y-89)*(y-89)<(76.2*76.2)):
            light_ray_list.append((x,y))
            ray_count=len(light_ray_list)
    if(use_diffuser):
        losses=transmission
    else:
        losses=1  
    parallel_angle =[]
    if(use_angle_filter):
        for a in angle:
            if(a<max_allowable_angle):    
                parallel_angle.append(a)
        angle=parallel_angle
        ray_count=len(angle)
    light_ray_intensity = (LED_intensity/rep)*ray_count*losses/(np.pi*(7.62*7.62)) 
    print(light_ray_intensity,'mw/cm^2')
print("plotting")
if (use_diffuser):
    x,y = zip(*cood_wafer)
else:
    x, y, thetax,thetay = zip(*cood_diffuser) 
x = np.array(x)
y = np.array(y)
# Create a figure with 2 plot areas
fig, axes = plt.subplots(ncols=2, nrows=1, figsize=(30, 10))
circle1 = plt.Circle((89, 89), 76.2, color='red',fill=False,linewidth=4.0)


axes[0].set_title('2D Histogram')
axes[0].hist2d(x, y, bins=nbins, cmap=plt.cm.BuGn_r)

axes[0].add_artist(circle1)

axes[1].hist(np.array(angle), bins=histbin)
