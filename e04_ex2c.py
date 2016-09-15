import numpy as np

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# load data
#bee_weight_all = pd.read_csv('data/bee_weight.csv', comment='#')
bee_sperm_all = pd.read_csv('data/bee_sperm.csv', comment='#')

bee_sperm_control = bee_sperm_all.loc[bee_sperm_all['Treatment']=='Control', ['Quality']]
bee_sperm_control = bee_sperm_control.dropna()
bee_sperm_pesticide = bee_sperm_all.loc[bee_sperm_all['Treatment']=='Pesticide', ['Quality']]
bee_sperm_pesticide = bee_sperm_pesticide.dropna()

# generate bootstrap
n_reps = 100000
bsc_replicates = np.empty(n_reps)
for i in range(n_reps):
    bsc_sample = np.random.choice(bee_sperm_control['Quality'], replace=True, size=len(bee_sperm_control))
    bsc_replicates[i] = np.std(bsc_sample)

# confidence interval
conf_int_bsc = np.percentile(bsc_replicates, [2.5, 97.5])

n_reps = 100000
bsp_replicates = np.empty(n_reps)
for i in range(n_reps):
    bsp_sample = np.random.choice(bee_sperm_pesticide['Quality'], replace=True, size=len(bee_sperm_pesticide))
    bsp_replicates[i] = np.std(bsp_sample)

# confidence interval
conf_int_bsp = np.percentile(bsp_replicates, [2.5, 97.5])

avg_bsc = np.mean(bee_sperm_control)
avg_bsp = np.mean(bee_sperm_pesticide)

print('Control Average:', avg_bsc)
print('Control 95th%:', conf_int_bsc)
print('Pesticide Average:', avg_bsp)
print('Pesticide 95th%:', conf_int_bsp)

def ecdf(data):
    '''
    Compute x,y values for an empirical distribution function
    '''

    x = np.sort(data)
    y = np.arange(1, 1+len(x)) / len(x)

    return x, y

# x_bsc, y_bsc = ecdf(bee_sperm_control)
# x_bsc = np.sort(x_bsc, axis=0)
# x_bsp, y_bsp = ecdf(bee_sperm_pesticide)
# x_bsp = np.sort(x_bsp, axis=0)
# #x_1975_bs, y_1975_bs = ecdf(bs_sample)
# plt.plot(x_bsc, y_bsc, marker='.', color = 'blue', linestyle='none', markersize=10, alpha=0.5)
# plt.plot(x_bsp, y_bsp, marker='.', color='red', linestyle='none', markersize=10, alpha=0.5)
# plt.xlabel('Sperm Quality')
# plt.ylabel('ECDF')
# plt.legend(('Control','Pesticide'), loc='lower right')
# plt.margins(0.02)
# plt.savefig('e04_ex2c.pdf', bbox_inches='tight')
# plt.show()
