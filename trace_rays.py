# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 17:22:47 2019

@author: evans
"""
import numpy as np
from myconfig import *

def trace_rays(LED_Grid,L,height):

    if (use_diffuser and use_angle_filter):
        print("calcuating diffuser scatter")
        (x1,y1,ax1,ay1) = first_step(LED_Grid,L) 
        (x1,y1,ax1,ay1) = diffuser_step(x1,y1,ax1,ay1,(height-L)) 
        return filter_step(x1,y1,ax1,ay1,(height-L))
    elif(use_diffuser):
        print("calcuating diffuser scatter")
        (x1,y1,ax1,ay1) = first_step(LED_Grid,L) 
        return diffuser_step(x1,y1,ax1,ay1,(height-L))      
    elif(use_angle_filter):
        print("calcuating filter scatter")
        (x1,y1,ax1,ay1) = first_step(LED_Grid,L) 
        return filter_step(x1,y1,ax1,ay1,(height-L)) 
    else:
        print("calcuating scatter")
        return first_step(LED_Grid,height)
        


def first_step(LED_Grid,distance):      
    x_full=[]
    y_full=[]
    thetax_full=[]
    thetay_full=[]
    mu, sigma = 0, LED_angle/2*(np.pi/180) # mean and standard deviation
    for LED in LED_Grid:
        x_pos,y_pos = LED[0],LED[1] # xy coordinates in a topdown view
        thetax = np.random.normal(mu, sigma, rep)
        x = x_pos + distance*(np.tan(thetax))
        thetay = np.random.normal(mu, sigma, rep)
        y =y_pos + distance*(np.tan(thetay))
        for x1,y1,dx,dy in zip(x,y,thetax,thetay):
            if (x1>0 and x1 < length and (y1>0 and y1 < width)):
                x_full.append(x1)
                y_full.append(y1)
                thetax_full.append(dx)
                thetay_full.append(dy)
                
                # if light ray outside of diffuser/wafer boundary then disgard
    return (x_full,y_full,thetax_full,thetay_full)

def diffuser_step(x,y,ax,ay,distance):
    x_full=[]
    y_full=[]
    thetax_full=[]
    thetay_full=[]
    mu, sigma = 0, diffuser_angle/2*(np.pi/180) # assumed normal distribution of light?
    dtx = ax + np.random.normal(mu, sigma, len(x)) # random values for x,y
    x = x + distance*(np.tan(dtx))
    dty = ay + np.random.normal(mu, sigma, len(y)) # random values for x,y
    y = y + distance*(np.tan(dty))
    for x1,y1,dx,dy in zip(x,y,dtx,dty):
        if (x1>0 and x1 < length and (y1>0 and y1 < width)):
            x_full.append(x1)
            y_full.append(y1)
            thetax_full.append(dx)
            thetay_full.append(dy)
    return (x_full,y_full,thetax_full,thetay_full)

def filter_step(x,y,ax,ay,distance):
    x_1=[]
    y_1=[]
    thetax_1=[]
    thetay_1=[]
    max_allowable_angle=(max_angle_degrees*np.pi/180) # degrees, max allowable optical angle
    for x1,y1,dx,dy in zip(x,y,ax,ay):
        if (dx < max_allowable_angle) and (dy < max_allowable_angle):
            x_1.append(x1)
            y_1.append(y1)
            thetax_1.append(dx)
            thetay_1.append(dy)
    x_1 = x_1 + distance*(np.tan(thetax_1))
    y_1 = y_1 + distance*(np.tan(thetay_1))
    x_full=[]
    y_full=[]
    thetax_full=[]
    thetay_full=[]
    for x1,y1,dx,dy in zip(x_1,y_1,thetax_1,thetay_1):
        if (x1>0 and x1 < length and (y1>0 and y1 < width)):
            x_full.append(x1)
            y_full.append(y1)
            thetax_full.append(dx)
            thetay_full.append(dy)
    return (x_full,y_full,thetax_full,thetay_full)
