# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 17:00:02 2019

@author: evans
"""
from scipy import stats
import numpy as np


def print_uniformity(x):
    print("calculating uniformity")
    
    ## Uniformity tests
    
    x1 = x[x < 153] # take subset inside circle 
    x2 =x1[x1 > 25]
       
    k=np.histogram(x2,bins=100)
    sd_error=((np.max(k[0])-np.mean((k[0])))/np.mean(k[0])*100) # standard error
    print("Standard Error = {} ".format(round(sd_error, 4)))
    std = np.std(k[0])/np.mean(k[0])
        
