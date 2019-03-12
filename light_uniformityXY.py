# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 11:36:22 2018

@author: evans
"""

import numpy as np 
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy import stats

 



## variables you can change 
x=16*16 # number of LEDs # hard coded for 16 by 16 # unused
spaceing = np.round(np.sqrt(x)) # unused 
LightW,LightL= 178, 178 # size of lightsource 
width,length = 178, 178 # size of mask 
L = 1 # distance between LED and diffuser
height = 10 # distance between LEDs and wafer
LED_intensity = 40 #  mw per LED
transmission = 0.6 # diffuser transmission
LED_angle = 30 # angle of LED beam (assumed 2 sd) 
diffuser_angle = 30 # angle of diffuser (assumed 2 sd) 
max_allowable_angle=10 # degrees, max allowable optical angle

use_diffuser = 0
intensity = 0
use_angle_filter=0 # calculate the final intensity after using a optical angle filter
plot=1
##

## simulation parameters
rep =1000 # light rays per LED
nbins = 1000 # bins for 2d hist
histbin = 10 #bins for angle hist
##


cood_xy = np.mgrid[0:LightW:16j, 0:LightL:16j].reshape(2,-1).T #hardcoded for 16 x 16
cood_diffuser =[]
cood_wafer =[]
angle =[]



if (use_diffuser):
    distance = L
    print("calcuating diffuser scatter")
else:
    distance = height 
    print("calcuating scatter")
  
    
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
    angle=[]
    test=[]
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
            test.append(((thetay+dty),(thetax+dtx)))
            angle.append(a*180/np.pi)
        
if (intensity):
    print("calcuating light wafer intensity (for diffuser)")
    light_ray_list=[]
    x_list=[]
    if (use_diffuser):
        wafer = cood_wafer
    else:
        x, y, thetax,thetay = zip(*cood_diffuser) 
        wafer = zip(x,y)
    for x,y in wafer:
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
    
#    x,y = zip(*light_ray_list)
#    x = np.array(x)
#    y = np.array(y)
#    fig, axes = plt.subplots(ncols=2, nrows=1, figsize=(30, 10))
#    counts, xedges, yedges, im = axes[0].hist2d(x, y, bins=nbins, cmap=plt.cm.BuGn_r)
#    j=np.mean(counts)
#    k=np.std(counts)
#    print(j)
#    print(k)
#    print(stats.kstest(x, 'uniform'))



    

if (use_diffuser):
    x,y = zip(*cood_wafer)
else:
    x, y, thetax,thetay = zip(*cood_diffuser) 
    
    
x = np.array(x)
y = np.array(y)

ax,ay = zip(*test)
ax = np.array(ax)*180/np.pi
ay = np.array(ay)*180/np.pi

print("calculating uniformity")

## Uniformity tests

x1 = x[x < 153]
x1 =x1[x1 > 25]
   
k=np.histogram(x1,bins=100)
print((np.max(k[0])-np.mean((k[0])))/np.mean(k[0])*100)
std = np.std(k[0])/np.mean(k[0])
    

##
   

if (plot):
    print("plotting graphs")

    # Create a figure with 2 plot areas
    fig, axes = plt.subplots(ncols=2, nrows=1, figsize=(30, 10))
    mpl.rcParams.update({'font.size': 22})
    font = {'family' : 'normal',
            'weight' : 'bold',
            'size'   : 22}
    
    circle1 = plt.Circle((89, 89), 76.2, color='red',fill=False,linewidth=4.0)

    
    axes[0].set_title('2D Histogram')
    counts, xedges, yedges, im = axes[0].hist2d(x, y, bins=nbins, cmap=plt.cm.BuGn_r)
    #print(counts)
    plt.colorbar(im, ax=axes[0])
    axes[0].set_xlabel("X distance (mm)")
    axes[0].set_ylabel("Y distance (mm)")
    axes[0].add_artist(circle1)
    
    axes[1].hist(np.abs(np.concatenate([ax, ay])), bins=histbin)
    axes[1].set_ylabel("Relative Intensity")
    axes[1].set_xlabel("Angle ($\degree$)")
    
    plt.figure(figsize=(16,10))
    #plt.hist(x1, bins=100)
    plt.hist2d(ax, ay, bins=nbins, cmap=plt.cm.BuGn_r)
    #print(stats.kstest(x, stats.uniform(loc=0.0, scale=178).cdf))
    plt.xlabel('X Angle ($\degree$)')
    plt.ylabel('Y Angle $\degree$')
    plt.grid(True)
    plt.axis((-75,75,-75,75))
    plt.colorbar()
    







  
  
  