import scipy.stats
import numpy as np
import matplotlib.pyplot as plt


# set matplotlib rc params
import seaborn as sns
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18, 'axes.titlesize' : 18}
sns.set(rc=rc) # updates rc file

def fold_change(c, RK, Kda=0.017, KdI=0.002, Kswitch=5.8):
    '''
    Compute fold change of data
    '''

    fold_change = (1 + ((RK * (1 + c/Kda)**2) / ((1 + c/Kda)**2 + Kswitch*(1 + c/KdI)**2)))**-1

    return fold_change
