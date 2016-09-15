import numpy as np

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# load data
bee_weight_all = pd.read_csv('data/bee_weight.csv', comment='#')
bee_sperm_all = pd.read_csv('data/bee_sperm.csv', comment='#')

bee_weight_control = bee_weight_all.loc[bee_weight_all['Treatment']=='Control', ['Weight']]
bee_weight_pesticide = bee_weight_all.loc[bee_weight_all['Treatment']=='Pesticide', ['Weight']]
# can also just import weight
# bee_weight_control = bee_weight_all.loc[bee_weight_all['Treatment']=='Control']['Weight']
# bee_weight_pesticide = bee_weight_all.loc[bee_weight_all['Treatment']=='Pesticide']['Weight']


avg_bwc = np.mean(bee_weight_control)
avg_bwp = np.mean(bee_weight_pesticide)

# generate bootstrap
n_reps = 100000
bwc_replicates = np.empty(n_reps)
for i in range(n_reps):
    bwc_sample = np.random.choice(bee_weight_control['Weight'], replace=True, size=len(bee_weight_control))
    bwc_replicates[i] = np.std(bwc_sample)

# confidence interval
conf_int_bwc = np.percentile(bwc_replicates, [2.5, 97.5])

n_reps = 100000
bwp_replicates = np.empty(n_reps)
for i in range(n_reps):
    bwp_sample = np.random.choice(bee_weight_pesticide['Weight'], replace=True, size=len(bee_weight_pesticide))
    bwp_replicates[i] = np.std(bwp_sample)

# confidence interval
conf_int_bwp = np.percentile(bwp_replicates, [2.5, 97.5])

print('Control Average:', avg_bwc)
print('Control 95th%:', conf_int_bwc)
print('Pesticide Average:', avg_bwp)
print('Pesticide 95th%:', conf_int_bwp)


def ecdf(data):
    '''
    Compute x,y values for an empirical distribution function
    '''

    x = np.sort(data)
    y = np.arange(1, 1+len(x)) / len(x)

    return x, y


# # plot the data
# x_bwc, y_bwc = ecdf(bee_weight_control)
# x_bwc = np.sort(x_bwc, axis=0)
# x_bwp, y_bwp = ecdf(bee_weight_pesticide)
# x_bwp = np.sort(x_bwp, axis=0)
# plt.plot(x_bwc, y_bwc, marker='.', color = 'blue', linestyle='none', markersize=15, alpha=0.5)
# plt.plot(x_bwp, y_bwp, marker='.', color = 'green', linestyle='none', markersize=15, alpha=0.5)
# plt.xlabel('bee weight')
# plt.ylabel('ECDF')
# plt.legend(('control','pesticide'), loc='upper left')
# plt.margins(0.02)
# plt.savefig('e04_ex2a.pdf', bbox_inches='tight')
# plt.show()
