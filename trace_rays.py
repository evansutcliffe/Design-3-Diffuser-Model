# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 17:22:47 2019

@author: evans
"""
import numpy as np
from myconfig import *

def trace_rays(cood_xy,distance):
    cood_diffuser =[]
    cood_wafer =[]

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
                # if light ray outside of diffuser/wafer boundary then disgard
    
      
                             
    if (use_diffuser):
        angle=[]
        distance = height - L;     
        mu, sigma = 0, diffuser_angle/2*(np.pi/180) # assumed normal distribution of light?
        random_theta = np.random.normal(mu, sigma, len(cood_diffuser)*2) # random values for x,y
        for i in range(len(cood_diffuser)):
            (x, y, thetax,thetay), dtx, dty  = cood_diffuser[i], random_theta[i], random_theta[i+len(cood_diffuser)]
            x = x + distance*(np.tan(thetax+dtx))
            y = y + distance*(np.tan(thetay+dty))        
            if (x>0 and x < length and (y>0 and y < width)):
                cood_wafer.append((x,y,(thetax+dtx),(thetay+dty)))
        return cood_wafer        
    else:         
        return cood_diffuser
      