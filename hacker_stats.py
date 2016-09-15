import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# load beak data
bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')
bd_2012 = np.loadtxt('data/beak_depth_scandens_2012.csv')

# bootstrap sample
# bs_sample = np.random.choice(bd_1975, replace=True, size=len(bd_1975))
# bs_replicate = np.mean(bs_sample)

def draw_bs_reps(data, n_reps, funct, size=1):
    '''
    bootstrap replicates
    '''

    bs_replicates = np.empty(n_reps)
    for i in range(n_reps):
        bs_sample = np.random.choice(data, replace=True, size=len(data))
        bs_replicates[i] = funct(bs_sample)

    # confidence interval
    conf_int = np.percentile(bs_replicates, [2.5, 97.5])

    print (conf_int)

    return bs_replicates


# # generate bootstrap
# n_reps = 100000
# bs_replicates_1975 = np.empty(n_reps)
# for i in range(n_reps):
#     bs_sample = np.random.choice(bd_1975, replace=True, size=len(bd_1975))
#     bs_replicates_1975[i] = np.std(bs_sample)
#
# # confidence interval
# conf_int_1975 = np.percentile(bs_replicates_1975, [2.5, 97.5])
#
# n_reps = 100000
# bs_replicates_2012 = np.empty(n_reps)
# for i in range(n_reps):
#     bs_sample = np.random.choice(bd_2012, replace=True, size=len(bd_2012))
#     bs_replicates_2012[i] = np.std(bs_sample)
#
# # confidence interval
# conf_int_2012 = np.percentile(bs_replicates_2012, [2.5, 97.5])
#
# def ecdf(data):
#     '''
#     Compute x,y values for an empirical distribution function
#     '''
#     x = np.sort(data)
#     y = np.arange(1, 1+len(x)) / len(x)
#     return x, y

# x_1975, y_1975 = ecdf(bd_1975)
# x_2012, y_2012 = ecdf(bd_2012)
# x_1975_bs, y_1975_bs = ecdf(bs_sample)
#
# plt.close()
# plt.plot(x_1975, y_1975, marker='.', linestyle='none')
# plt.plot(x_1975_bs, y_1975_bs, marker='.', linestyle='none', alpha=0.5)
# plt.xlabel('beak depth (mm)')
# plt.ylabel('ECDF')
# plt.legend(('1975','bootstrap'), loc='lower right')
# plt.show()
