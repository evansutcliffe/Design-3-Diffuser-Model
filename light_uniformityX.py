# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 11:36:22 2018

@author: evans
"""

import numpy as np 
import matplotlib.pyplot as plt

#shows the binned data of the light intensity on the wafer 
# intensity drops of at the edges and shows slight ripple around the mean

width,length = 178, 178
height = 20 # must be greater than L (total distance between source and wafer)
L = 1     # distance between source and diffuser

cood_xy = np.mgrid[0:width:16j, 0:length:16j].reshape(2,-1).T
cood_diffuser =[]
cood_wafer =[]

mu, sigma = 0, 15*(np.pi/180) # mean and standard deviation for single dim
rep =1000 # rays per LED
light_ray_intensity = 40/rep #mw

bin_size=500 # for graphing only

for LED in cood_xy:
    x,y = LED[0],LED[1]
    theta = np.random.normal(mu, sigma, rep)
    deltax = L*(np.tan(theta))
    for i in range(rep):
        if (deltax[i]+x>0 and x+deltax[i] < width):
            cood_diffuser.append((x+deltax[i],theta[i]))
mu, sigma = 0, 15*(np.pi/180)
 
random_theta = np.random.normal(mu, sigma, len(cood_diffuser))
for i in range(len(cood_diffuser)):
    (x, theta), delta_theta = cood_diffuser[i], random_theta[i]
    deltax = (height-L)*(np.tan(delta_theta))
    if (deltax+x>0 and x+deltax < width):
        cood_wafer.append((x+deltax,theta+delta_theta))


#pyl.figure(figsize=(15,15))
x,theta = zip(*cood_wafer)
x=np.array(x)
plt.figure(figsize=(15,15))
plt.hist(x, bins=bin_size)




  
  
  