import scipy.stats
import numpy as np
import matplotlib.pyplot as plt


# set matplotlib rc params
import seaborn as sns
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18, 'axes.titlesize' : 18}
sns.set(rc=rc) # updates rc file

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

# plot the data
plt.close()
plt.semilogx(wt_iptg, wt_foldchange, marker='.', linestyle='none', markersize=20)
plt.semilogx(q18m_iptg, q18m_foldchange, marker='.',  linestyle='none', markersize=20)
plt.semilogx(q18a_iptg, q18a_foldchange, marker='.',  linestyle='none', markersize=20)
plt.xlabel('IPTG (mM)')
plt.ylabel('Fold Change')
plt.legend(('wild type', 'Q18M', 'Q18A'), loc='lower right')

# save the figure
plt.savefig('e03_ex2.pdf', bbox_inches='tight')
plt.show()
