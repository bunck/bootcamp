import numpy as np

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

gr_data = pd.read_csv('data/grant_complete.csv', comment='#')
#gr_beakdepth_1987 = gr_data.loc[gr_data['year']==1987,['beak depth (mm)']]


for year in [1973, 1975, 1987, 1991, 2012]:
    gr_bd_fortis = gr_data.loc[(gr_data['year']==year) & (gr_data['species']=='fortis'), ['beak depth (mm)']]
    gr_bd_scandens = gr_data.loc[(gr_data['year']==year) & (gr_data['species']=='scandens'), ['beak depth (mm)']]
    gr_bl_fortis = gr_data.loc[(gr_data['year']==year) & (gr_data['species']=='fortis'), ['beak length (mm)']]
    gr_bl_scandens = gr_data.loc[(gr_data['year']==year) & (gr_data['species']=='scandens'), ['beak length (mm)']]
    plt.plot(gr_bl_fortis, gr_bd_fortis, marker='.', color = 'blue', linestyle='none', markersize=10, alpha=0.5)
    plt.plot(gr_bl_scandens, gr_bd_scandens, marker='.', color='red', linestyle='none', markersize=10, alpha=0.5)

    plt.xlabel('beak length (mm)')
    plt.ylabel('beak width (mm)')
    plt.legend(('fortis','scandens'), loc='lower right')
    # plt.savefig('e04_ex1e_{year:d}.pdf'.format(year=year), bbox_inches='tight')
    # plt.close()

def ecdf(data):
    '''
    Compute x,y values for an empirical distribution function
    '''

    x = np.sort(data)
    y = np.arange(1, 1+len(x)) / len(x)

    return x, y

# x_gr_bl_87_fortis, y_gr_bl_87_fortis = ecdf(gr_bl_87_fortis)
# x_gr_bl_87_scandens, y_gr_bl_87_scandens = ecdf(gr_bl_87_scandens)
#x_1975_bs, y_1975_bs = ecdf(bs_sample)

# plt.xlabel('beak length (mm)')
# plt.ylabel('beak width (mm)')
# plt.legend(('fortis','scandens'), loc='lower right')
plt.savefig('e04_ex1e.pdf', bbox_inches='tight')
plt.show()
