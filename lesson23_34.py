import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import seaborn as sns

# set matplotlib rc params
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18, 'axes.titlesize' : 18}
sns.set(rc=rc) # updates rc file

data_txt = np.loadtxt('data/collins_switch.csv', delimiter=',', skiprows=2)

# # slice out iptg, gfp, and error bars
iptg = data_txt[:,0]
gfp = data_txt[:,1]
sem = data_txt[:,2]


# # plot iptg vs gfp
# plt.semilogx(iptg, gfp, linestyle='none', marker='.', markersize=20)
# plt.xlabel('IPTG (µM)')
# plt.ylabel('Normalized GFP')
# plt.title('IPTG Titration - semilog X')
# plt.ylim(-0.02, 1.02)
# plt.xlim(8e-4, 15)
# plt.show()

# # plot iptg vs gfp
# plt.errorbar(iptg, gfp, yerr=sem, linestyle='none', marker='.', markersize=20)
# plt.xlabel('IPTG (µM)')
# plt.ylabel('Normalized GFP')
# plt.title('IPTG Titration - semilog X w/ ErrorBars')
# plt.ylim(-0.02, 1.02)
# plt.xlim(8e-4, 15)
# plt.xscale('log') # plotting function defaults to linear scaling
# plt.show()

# practice exercise 3
