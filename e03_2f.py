import scipy.stats
import numpy as np
import matplotlib.pyplot as plt


# set matplotlib rc params
import seaborn as sns
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18, 'axes.titlesize' : 18}
sns.set(rc=rc) # updates rc file

# generate theoretical concentration
conc_theor = np.logspace(-6, 2, 50)
conc_bohr = np.linspace(-6, 6, 50)
rk_wt = 141.5
rk_q18a = 16.56
rk_q18m = 1332

# import data
wt_data = np.loadtxt('data/wt_lac.csv', delimiter=',', skiprows=3)
q18m_data = np.loadtxt('data/q18m_lac.csv', delimiter=',', skiprows=3)
q18a_data = np.loadtxt('data/q18a_lac.csv', delimiter=',', skiprows=3)

# break data into x,y
wt_iptg = wt_data[:,0]
wt_foldchange = wt_data[:,1]
q18m_iptg = q18m_data[:,0]
q18m_foldchange = q18m_data[:,1]
q18a_iptg = q18a_data[:,0]
q18a_foldchange = q18a_data[:,1]

# calculate theoretical fold change
def fold_change(c, RK, Kda=0.017, KdI=0.002, Kswitch=5.8):
    '''
    Compute fold change of data
    '''

    fold_change_calc = (1 + ((RK * (1 + c/Kda)**2) / ((1 + c/Kda)**2 + Kswitch*(1 + c/KdI)**2)))**-1

    return fold_change_calc

# plot it!
def plot_fold_change(wt_y, q18a_y, q18m_y):

    # plot the data
    plt.close()
    plt.semilogx(conc_theor, wt_y, linestyle='solid')
    plt.semilogx(conc_theor, q18m_y, linestyle='solid')
    plt.semilogx(conc_theor, q18a_y, linestyle='solid')
    plt.xlabel('IPTG (mM)')
    plt.ylabel('Fold Change')
    plt.legend(('wild type', 'Q18M', 'Q18A'), loc='lower right')

    plt.savefig('e03_ex2e.pdf', bbox_inches='tight')
    plt.show()

# calculates Bohr parameter from concentration
def bohr_parameter(c, RK, Kda=0.017, KdI=0.002, Kswitch=5.8):

    bohring = -np.log(RK) - np.log(((1 + c/Kda)**2) / ((1 + c/Kda)**2 + Kswitch*(1 + c/KdI)**2))

    return bohring

# calculates fold chance from the bohr parameter
def fold_change_bohr(c_wt, RK_wt, c_q18a, RK_q18a, c_q18m, RK_q18m):

    bohr_param_wt = bohr_parameter(c_wt, RK_wt)
    bohr_param_q18a = bohr_parameter(c_q18a, RK_q18a)
    bohr_param_q18m = bohr_parameter(c_q18m, RK_q18m)

    fold_change_wt = 1 / (1 + np.exp(-1 * bohr_param_wt))
    fold_change_q18a = 1 / (1 + np.exp(-1 * bohr_param_q18a))
    fold_change_q18m = 1 / (1 + np.exp(-1 * bohr_param_q18m))

    # plot the data
    plt.close()
    #plot theoretical
    bohr_x = np.linspace(-6, 6, 50)
    fold_change = 1 / (1 + np.exp(-1 * bohr_x))
    plt.plot(bohr_x, fold_change, linestyle='solid')

    plt.plot(bohr_param_wt, wt_foldchange, marker='.', linestyle='none', markersize=20)
    plt.plot(bohr_param_q18a, q18a_foldchange, marker='.', linestyle='none', markersize=20)
    plt.plot(bohr_param_q18m, q18m_foldchange, marker='.', linestyle='none', markersize=20)
    plt.xlabel('Bohr Parameter')
    plt.ylabel('Fold Change')

    plt.savefig('e03_ex2f.pdf', bbox_inches='tight')
    plt.show()

    return bohr_param_wt, bohr_param_q18a, bohr_param_q18m
