import numpy as np

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# part a
impact_force_ii = df.loc[df['ID']=='II', ['impact force (mN)']]
impact_force_ii_avg = np.average(impact_force)

# part b
impact_force_i = df.loc[df['ID']=='I', ['impact force (mN)']]
impact_force_i_avg = np.average(impact_force)

impact_force_iii = df.loc[df['ID']=='III', ['impact force (mN)']]
impact_force_iii_avg = np.average(impact_force)

impact_force_iv = df.loc[df['ID']=='IV', ['impact force (mN)']]
impact_force_iv_avg = np.average(impact_force)
