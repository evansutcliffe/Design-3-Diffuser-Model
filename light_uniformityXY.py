# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 11:36:22 2018

@author: evans
"""

import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import kde
from matplotlib.patches import Ellipse
 



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
use_diffuser = 1
intensity = 1
##

## simulation parameters
rep =1000 # light rays per LED
nbins = 1000 # bins for charts
histbin = 100 #bins for histogram
##


cood_xy = np.mgrid[0:LightW:16j, 0:LightL:16j].reshape(2,-1).T #hardcoded for 16 x 16
cood_diffuser =[]
cood_wafer =[]
angle =[]

mu, sigma = 0, LED_angle/2*(np.pi/180) # mean and standard deviation


if (use_diffuser):
    distance = height
    print("calcuating diffuser")
else:
    distance = L
    print("calcuating wafer")
for LED in cood_xy:
    x,y = LED[0],LED[1]
    thetax = np.random.normal(mu, sigma, rep)
    x = x + L*(np.tan(thetax))
    thetay = np.random.normal(mu, sigma, rep)
    y =y+ L*(np.tan(thetay))
    for i in range(rep):
        if (x[i]>0 and x[i] < length and (y[i]>0 and y[i] < width)):
            cood_diffuser.append((x[i],y[i],thetax[i],thetay[i]))
mu, sigma = 0, LED_angle/2*(np.pi/180) # change to T- dist ?    
if (use_diffuser):
    L = height -L;     
    print("calcuating wafer")
    random_theta = np.random.normal(mu, sigma, len(cood_diffuser)*2)
    for i in range(len(cood_diffuser)):
        (x, y, thetax,thetay), dtx, dty  = cood_diffuser[i], random_theta[i], random_theta[i+len(cood_diffuser)]
        x= x+ height*(np.tan(thetax+dtx))
        y = y+ height*(np.tan(thetay+dty))
        a = np.sqrt((thetay+dty)*(thetay+dty)+(thetax+dtx)*(thetax+dtx))
        if (x>0 and x < length and (y>0 and +y < width)):
            cood_wafer.append((x,y))
            angle.append(a*180/np.pi)

if (intensity):
    light_ray_list=[]
    for x,y in cood_wafer:
        if ((x-89)*(x-89)+(y-89)*(y-89)<(76.2*76.2)):
            light_ray_list.append((x,y))
    light_ray_intensity = LED_intensity/rep
    print(len(light_ray_list)*light_ray_intensity*transmission/(7.62*7.62))
    print(len(light_ray_list))
    print(len(cood_wafer))
print("plotting")
if (use_diffuser):
    x,y = zip(*light_ray_list)
else:
    x, y, thetax,thetay = zip(*light_ray_list)
x = np.array(x)
y = np.array(y)
# Create a figure with 6 plot areas
fig, axes = plt.subplots(ncols=4, nrows=1, figsize=(21, 5))
circle1 = plt.Circle((89, 89), 76.2, color='red',fill=False)
circle2 = plt.Circle((89, 89), 76.2, color='red',fill=False)
circle3 = plt.Circle((89, 89), 76.2, color='red',fill=False) 

# Thus we can cut the plotting window in several hexbins


axes[0].set_title('2D Histogram')
axes[0].hist2d(x, y, bins=nbins, cmap=plt.cm.BuGn_r)

axes[0].add_artist(circle1)

#axes[1].set_title('2D Histogram')
#x1,y1 = zip(*light_ray_list)
#
#axes[1].hist2d(np.array(x1), np.array(y1), bins=nbins, cmap=plt.cm.BuGn_r)
#axes[0].add_artist(circle1)


  
## Evaluate a gaussian kde on a regular grid of nbins x nbins over data extents
#k = kde.gaussian_kde((x,y))
#xi, yi = np.mgrid[x.min():x.max():nbins*1j, y.min():y.max():nbins*1j]
#zi = k(np.vstack([xi.flatten(), yi.flatten()]))
# 
## plot a density
#axes[1].set_title('Calculate Gaussian KDE')
#axes[1].pcolormesh(xi, yi, zi.reshape(xi.shape), cmap=plt.cm.BuGn_r)
#axes[1].add_artist(circle2)
# 
#
#axes[2].set_title('Contour')
#axes[2].pcolormesh(xi, yi, zi.reshape(xi.shape), shading='gouraud', cmap=plt.cm.BuGn_r)
#axes[2].contour(xi, yi, zi.reshape(xi.shape) )
#axes[2].add_artist(circle3)

axes[3].hist(np.array(angle), bins=histbin)




  
  
  