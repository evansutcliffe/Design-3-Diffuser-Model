# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 17:00:02 2019

@author: evans
"""
from scipy import stats
import numpy as np


def print_uniformity(data):
    print("calculating uniformity")
    x,y,ax,ay = data[:,0],data[:,1],data[:,2],data[:,3]
    ## Uniformity tests
    
    x = x[25 < x] # take subset inside circle 
    x = x[x < 153]
    k=np.histogram(x,bins=100)
    sd_error=((np.max(k[0])-np.mean((k[0])))/np.mean(k[0])*100) # standard error
    print("Standard Error = {} ".format(round(sd_error, 4)))
    std = np.std(k[0])/np.mean(k[0])
        
