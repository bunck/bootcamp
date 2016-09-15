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

    # # import data
    # wt_data = np.loadtxt('data/wt_lac.csv', delimiter=',', skiprows=3)
    # q18m_data = np.loadtxt('data/q18m_lac.csv', delimiter=',', skiprows=3)
    # q18a_data = np.loadtxt('data/q18a_lac.csv', delimiter=',', skiprows=3)
    #
    # # break data into x,y
    # wt_iptg = wt_data[:,0]
    # wt_foldchange = wt_data[:,1]
    # q18m_iptg = q18m_data[:,0]
    # q18m_foldchange = q18m_data[:,1]
    # q18a_iptg = q18a_data[:,0]
    # q18a_foldchange = q18a_data[:,1]
    #
    # # plot the data
    # plt.semilogx(wt_iptg, wt_foldchange, marker='.', linestyle='none', markersize=20)
    # plt.semilogx(q18m_iptg, q18m_foldchange, marker='.',  linestyle='none', markersize=20)
    # plt.semilogx(q18a_iptg, q18a_foldchange, marker='.',  linestyle='none', markersize=20)
    # plt.legend(('theor WT', 'theor Q18M', 'theor Q18A', 'wild type', 'Q18M', 'Q18A'), loc='upper left')
    #
    # save the figure
    plt.savefig('e03_ex2e.pdf', bbox_inches='tight')
    plt.show()

def bohr_parameter(c, RK, Kda=0.017, KdI=0.002, Kswitch=5.8):

    bohring = -np.log(RK) - np.log(((1 + c/Kda)**2) / ((1 + c/Kda)**2 + Kswitch*(1 + c/KdI)**2))

    return bohring


def fold_change_bohr(bohr_param):

    #bohr_param = bohr_parameter(c, RK)

    fc_bohr_calc = 1 / (1 + np.exp(-1 * bohr_param))

    # plot the data
    plt.close()
    plt.plot(bohr_param, fc_bohr_calc, linestyle='solid')
    plt.xlabel('Bohr Parameter')
    plt.ylabel('Fold Change')

    plt.savefig('e03_ex2e.pdf', bbox_inches='tight')
    plt.show()




    return fc_bohr_calc
