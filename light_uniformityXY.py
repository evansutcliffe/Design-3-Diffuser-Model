# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 11:36:22 2018
@author: evans
"""

import numpy as np 
import matplotlib as mpl
import matplotlib.pyplot as pyl


x= 256 # number of LEDs
width,length = 178, 178
L = 35


xy = np.mgrid[0:width:16j, 0:length:16j].reshape(2,-1).T
diffusertheta = []
diffuserx = []
std_list =[]

mu, sigma = 0, 15*(np.pi/180) # mean and standard deviation
 # for single dim
rep =100
light_ray_intensity = 40/rep #mw
for L in range (0,34):
    for LED in xy:
        x,y = LED[0],LED[1]
        theta = np.random.normal(mu, sigma, rep)
        deltax = L*(np.tan(theta))
        for i in range(rep):
            if (deltax[i]+x>0 and x+deltax[i] < width):
                diffuserx.append(x+deltax[i])
                diffusertheta.append(theta[i])
    mu, sigma = 0, 15*(np.pi/180) # change to T- dist ?    
    height = 35-L     
    diffusertheta2 = []
    diffuserx2 = []
    std_list2 =[]
    random_theta = np.random.normal(mu, sigma, len(diffuserx))
    for i in range(len(diffuserx)):
        x, theta, r_theta = diffuserx[i],diffusertheta[i], random_theta[i]
        delta_theta = r_theta + theta
        deltax = height*(np.tan(delta_theta))
        if (deltax+x>0 and x+deltax < width):
            diffuserx2.append(x+deltax)
            diffusertheta2.append(theta)
    standardd = np.std(np.array(diffuserx2))     
    std_list.append(standardd)            
    print(L)
pyl.figure(figsize=(15,15))

#plt.pcolormesh(xi, yi, zi.reshape(xi.shape))
p#yl.plot(std_list)
mpl.pyplot.hist(diffuserx2, bins=300)
#pyl.figure(figsize=(15,15))
#mpl.pyplot.hist(diffuserx, bins=300)
  
  
