# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 17:08:35 2019

@author: evans
"""
from myconfig import *
import numpy as np

def intensity(wafer):
    if (intensity):
        print("calcuating light wafer intensity (for diffuser)")
        light_ray_list=[]
        x_list=[]

        print("")
        ray_list=0
        angle_count=0
        for x,y,thetax,thetay in wafer:
            if ((x-89)*(x-89)+(y-89)*(y-89)<(76.2*76.2)):
                ray_list=ray_list+1
                if(use_angle_filter and (thetax <max_allowable_angle) and (thetay < max_allowable_angle)):
                    angle_count=angle_count+1
        if(use_diffuser):
            losses=transmission
        else:
            losses=1  
        if (use_angle_filter):
            ray_count=angle_count
        else:
            ray_count=ray_list
    
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
