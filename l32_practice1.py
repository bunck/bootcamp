import numpy as np

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

[df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')]

df_big_force = df[df['impact force (mN)'] > 1000]
df_big_force.loc[:,['impact time (ms)']]

# part a
df.loc[np.abs(df['adhesive strength (Pa)']) > 2000,['impact time (ms)']]

# part b
df.loc[df['ID']=='II', ['impact force (mN)', 'adhesive force (mN)']]

# part c
df.loc[df['ID']=='III', ['adhesive force (mN)', 'time frog pulls on target (ms)']]
df.loc[(df['ID']=='III') | (df['ID']=='IV'), ['adhesive force (mN)', 'time frog pulls on target (ms)']]
