import numpy as np

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

gr_1973 = pd.read_csv('data/grant_1973.csv', comment='#')
gr_1975 = pd.read_csv('data/grant_1975.csv', comment='#')
gr_1987 = pd.read_csv('data/grant_1987.csv', comment='#')
gr_1991 = pd.read_csv('data/grant_1991.csv', comment='#')
gr_2012 = pd.read_csv('data/grant_2012.csv', comment='#')

# fixing 1973 data
gr_1973 = gr_1973.rename(columns = {'yearband' : 'year'})
gr_1973.loc[:,'year'] = 1973

# add years to other data
gr_1975.loc[:,'year'] = 1975
gr_1987.loc[:,'year'] = 1987
gr_1991.loc[:,'year'] = 1991
gr_2012.loc[:,'year'] = 2012

# rename columns
gr_1973 = gr_1973.rename(columns = {'beak length' : 'beak length (mm)'})
gr_1973 = gr_1973.rename(columns = {'beak depth' : 'beak depth (mm)'})

gr_1975 = gr_1975.rename(columns = {'Beak length, mm' : 'beak length (mm)'})
gr_1975 = gr_1975.rename(columns = {'Beak depth, mm' : 'beak depth (mm)'})

gr_1987 = gr_1987.rename(columns = {'Beak length, mm' : 'beak length (mm)'})
gr_1987 = gr_1987.rename(columns = {'Beak depth, mm' : 'beak depth (mm)'})

gr_1991 = gr_1991.rename(columns = {'blength' : 'beak length (mm)'})
gr_1991 = gr_1991.rename(columns = {'bdepth' : 'beak depth (mm)'})

gr_2012 = gr_2012.rename(columns = {'blength' : 'beak length (mm)'})
gr_2012 = gr_2012.rename(columns = {'bdepth' : 'beak depth (mm)'})

gr_combined = pd.concat([gr_1973, gr_1975, gr_1987, gr_1991, gr_2012], ignore_index=True, axis=0)

# remove duplicates
gr_combined_clean = gr_combined.drop_duplicates(subset = ['band', 'year'])

# save to csv, note need '.csv' to include file extension
gr_combined_clean.to_csv('gr_combined_clean.csv', index=False)
