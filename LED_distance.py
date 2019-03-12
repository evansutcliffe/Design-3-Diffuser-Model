# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 11:36:22 2018

@author: evans
"""

import numpy as np 
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import stats

x= 256 # number of LEDs
width,length = 178, 178
rep =1000

xy = np.mgrid[0:width:30j, 0:length:30j].reshape(2,-1).T
d_list =[]
d_list1 =[]
mu, sigma = 0, 15/2*(np.pi/180) # mean and standard deviation
 # for single dim
ran = range(10,150,5)
for L in ran: 
    diffuserx=[]
    diffusertheta=[]
    for LED in xy:
        x,y = LED[0],LED[1]
        theta = np.random.normal(mu, sigma, rep)
        deltax = L*(np.tan(theta))
        for i in range(rep):
            if (deltax[i]+x>0 and x+deltax[i] < width):
                diffuserx.append(x+deltax[i])
                diffusertheta.append(theta[i])
    x=np.array(diffuserx)
    x1 = x[x > 25]
    x1 =x1[x1 < 153]
    k=np.histogram(x1,bins=100)
    counts=k[0]
    std = np.std(counts/np.mean(counts))
    k=np.histogram(diffuserx,bins=100)
    counts=k[0]
    std1 = np.std(counts/np.mean(counts))
    #[d, p]=stats.kstest(diffuserx, 'uniform', args=(0, 178))
    d_list.append(std)
    d_list1.append(std1)
    if (L%10 == 0):
        print(L)
        print(std1)


plt.figure(figsize=(16,10))
mpl.rcParams.update({'font.size': 22})
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}
plt.plot(ran,d_list/max(d_list),color='darkgreen')
plt.plot(ran,d_list1/max(d_list),color='blue')
#plt.plot((d_list/max(d_list)))
plt.xlabel('Z Distance ($mm$)')
plt.ylabel('Normalised coefficient of variation $C_v$')
plt.grid(True)
#plt.axis((0,150,0,1))
plt.show()




  
  
  