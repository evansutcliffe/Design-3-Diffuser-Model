
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


def plot_data(x,y,ax,ay,nbins,histbin):
    
    print("plotting graphs")

    # Create a figure with 2 plot areas
    fig, axes = plt.subplots(ncols=2, nrows=1, figsize=(30, 10))
    mpl.rcParams.update({'font.size': 22})
    font = {'family' : 'normal',
            'weight' : 'bold',
            'size'   : 22}
    
    circle1 = plt.Circle((89, 89), 76.2, color='red',fill=False,linewidth=4.0)

    
    axes[0].set_title('2D Histogram')
    counts, xedges, yedges, im = axes[0].hist2d(x, y, bins=nbins, cmap=plt.cm.BuGn_r)
    #print(counts)
    plt.colorbar(im, ax=axes[0])
    axes[0].set_xlabel("X distance (mm)")
    axes[0].set_ylabel("Y distance (mm)")
    axes[0].add_artist(circle1)
    
    axes[1].hist(np.abs(np.concatenate([ax, ay])), bins=histbin)
    axes[1].set_ylabel("Relative Intensity")
    axes[1].set_xlabel("Angle ($\degree$)")
    
    
#    plt.figure(figsize=(16,10))
#    #plt.hist(x1, bins=100)
#    plt.hist2d(ax, ay, bins=nbins, cmap=plt.cm.BuGn_r)
#    #print(stats.kstest(x, stats.uniform(loc=0.0, scale=178).cdf))
#    plt.xlabel('X Angle ($\degree$)')
#    plt.ylabel('Y Angle $\degree$')
#    plt.grid(True)
#    plt.axis((-75,75,-75,75))
#    plt.colorbar()