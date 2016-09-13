import numpy as np

xa_high = np.loadtxt('data/xa_high_food.csv', comments = '#')
xa_lox = np.loadtxt('data/xa_low_food.csv', comments = '#')

def xa_to_diameter(xa):
    '''
    convert array of x-sectional areas to diameters with commensurate units
    '''

    #couple diameter from area

    #A = pi * d^2 / 4
    diameter =  np.sqrt(xa *4 / np.pi)
