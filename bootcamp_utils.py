# bootcamp utils: a collection of statistical functions
import numpy as np

# This is how we import the module of Matplotlib we'll be using
import matplotlib.pyplot as plt

# Some pretty Seaborn settings
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# The following is specific Jupyter notebooks
# %matplotlib inline
# %config InlineBackend.figure_formats = {'png', 'retina'}


def ecdf(data):
    '''
    Compute x,y values for an empirical distribution function
    '''

    x = np.sort(data)
    y = np.arange(1, 1+len(x)) / len(x)

    return x, y

def draw_bs_reps(data, n_reps, funct, size=1):
    '''
    bootstrap replicates
    '''

    bs_replicates = np.empty(n_reps)
    for i in range(n_reps):
        bs_sample = np.random.choice(data, replace=True, size=len(data))
        bs_replicates[i] = funct(bs_sample)

    conf_int = np.percentile(bs_replicates, [2.5, 97.5])

    print (conf_int)
    return bs_replicates
