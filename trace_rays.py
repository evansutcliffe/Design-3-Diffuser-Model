# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 17:22:47 2019

@author: evans
"""
import numpy as np
from myconfig import *

def def_rep(r):
    global rep
    rep = r



def trace_rays(LED_Grid,L,height):

    if (use_diffuser and use_angle_filter):
        print("calcuating diffuser scatter")
        data = first_step(LED_Grid,L) 
        data = diffuser_step(data,(height-L)) 
        return filter_step(data,(height-L))
    elif(use_diffuser):
        print("calcuating diffuser scatter")
        data = first_step(LED_Grid,L)
        return diffuser_step(data,(height-L))      
    elif(use_angle_filter):
        print("calcuating filter scatter")
        data = first_step(LED_Grid,L) 
        return filter_step(data,(height-L)) 
    else:
        print("calcuating scatter")
        return first_step(LED_Grid,height)
        


def first_step(LED_Grid,distance): 
    x,y = zip(*LED_Grid)
    x= np.tile(x,rep)
    y= np.tile(y,rep)
    data = np.zeros((LED_count*rep,4))
    mu, sigma = 0, LED_angle/2*(np.pi/180) # mean and standard deviation
    data[:,2] = np.random.normal(mu, sigma, LED_count*rep)
    data[:,3] = np.random.normal(mu, sigma, LED_count*rep)
    data[:,0] = x + distance*(np.tan(data[:,2]))
    data[:,1] = y + distance*(np.tan(data[:,3]))
    data= data[np.where((0 <= data[:,0]) & (data[:,0] <= length) & (0 <= data[:,1]) & (data[:,1] <= width))] 
    return  data

def diffuser_step(old_data,distance):
    data = np.zeros(old_data.shape)
    mu, sigma = 0, diffuser_angle/2*(np.pi/180) # assumed normal distribution of light?
    #data[:,2] =np.sum(old_data[:,2], np.random.normal(mu, sigma, old_data.shape[0])) # random values
    data[:,2] = old_data[:,2] + np.random.normal(mu, sigma, old_data.shape[0]) # random valuesfor x,y
    data[:,3] = old_data[:,3] + np.random.normal(mu, sigma, old_data.shape[0]) # random valuesfor x,y
    data[:,0] = old_data[:,0] + distance*(np.tan(data[:,2]))
    data[:,1] = old_data[:,1] + distance*(np.tan(data[:,3]))
    data= data[np.where((0 <= data[:,0]) & (data[:,0] <= length) & (0 <= data[:,1]) & (data[:,1] <= width))] 
    return data

def filter_step(old_data,distance):
    max_allowable_angle=(max_angle_degrees*np.pi/180) # degrees, max allowable optical angle
    old_data= old_data[np.where((old_data[:,2] <= max_allowable_angle) & (old_data[:,3] <= max_allowable_angle))]  
    data = np.zeros(old_data.shape)
    data[:,2] = old_data[:,2]
    data[:,3] = old_data[:,3]
    data[:,0] = old_data[:,0] + distance*(np.tan(data[:,2]))
    data[:,1] = old_data[:,1] + distance*(np.tan(data[:,3]))
    data= data[np.where((0 <= data[:,0]) & (data[:,0] <= length) & (0 <= data[:,1]) & (data[:,1] <= width))] 
    return data

