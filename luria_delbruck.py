import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# specify parameters
# number of generations
n_gen = 16

# chance of having beneficial mutation
r = 1e-5

# total number of cells
n_cells = 2**(n_gen-1)

# adaptive immunity samples
ai_samples = np.random.binomial(n_cells, r, size=100000)

# report mean and standard deviation
print('AI Mean:', np.mean(ai_samples))
print('AI std:', np.std(ai_samples))
print('AI Fano:', np.var(ai_samples) / np.mean(ai_samples))

# funciton to draw out of random mutation

def draw_random_mutation(n_gen, r):
    """Draw sample under random mutation hypothesis"""
    # initialize number of mutaitons
    n_mut = 0

    for g in range(n_gen):
        n_mut = 2*n_mut + np.random.binomial(2**g - 2*n_mut, r)

    return n_mut

def sample_random_mutation(n_gen, r, size=1):
    # initialize samples
    samples = np.empty(size)

    # draw the samples
    for i in range(size):
        samples[i] = draw_random_mutation(n_gen, r)

    return samples


rm_samples = sample_random_mutation(n_gen, r, size=100000)

print('AI Mean:', np.mean(rm_samples))
print('AI std:', np.std(rm_samples))
print('AI Fano:', np.var(rm_samples) / np.mean(rm_samples))
