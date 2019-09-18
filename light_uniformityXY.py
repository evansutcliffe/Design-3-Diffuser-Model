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
import time

import matplotlib.pyplot as plt
import matplotlib as mpl

# top down view of intensity on a wafer
# input distance and other variables in config files
norm = []
numpy =[]
 
    
def run_prog():
    t0 = time.clock()
    LED_Grid = np.mgrid[0:LightW:dim_x*1j, 0:LightL:dim_y*1j].reshape(2,-1).T # e.g. 16 x 16 LED grids
    t1=time.clock()
    data=trace_rays.trace_rays(LED_Grid,L,height)
    data[:,2],data[:,3]  = data[:,2]*180/np.pi, data[:,3]*180/np.pi

    t2 = time.clock()
    #print("calcuating light wafer intensity (for diffuser)")
    #print("")
    wafer_data = light_ray_intensity.intensity(data)   
    
    

    t3 = time.clock()
    #myconfig.save_data(data)
    
    print_uniformity.print_uniformity(data)
    
    t4 = time.clock()
    print("plotting graphs")
    print("")
    plot_data.plot_data(data)
    plot_data.plot_data(wafer_data)
    
    t5 = time.clock()
    
    
    print("setup:"+str((t1-t0)*1000)+"ms")
    print("calc rays :"+str((t2-t1)*1000)+"ms")
    print("calc intensity:"+str((t3-t2)*1000)+"ms")
    print("calc statistics:"+str((t4-t3)*1000)+"ms")
    print("plot:"+str((t5-t4)*1000)+"ms")
    norm.append((t2-t1)*1000)
    numpy.append((t3-t2)*1000)

repeat=0
if(repeat):
    rang = np.arange(1,16)
    meas = 2**rang
    #reps =[0,1]
    for m in meas:
        trace_rays.def_rep(m)
        run_prog()
    print(np.c_[norm, numpy])
    fig, ax = plt.subplots(figsize=(15,15))
    plt.plot(reps,norm)
    plt.plot(reps,numpy)   
else:
    run_prog()

  
  
  