import numpy as np

xa_high = np.loadtxt('data/xa_high_food.csv', comments = '#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments = '#')

def xa_to_diameter(xa):
    '''
    convert array of x-sectional areas to diameters with commensurate units
    '''

    #couple diameter from area

    #A = pi * d^2 / 4
    diameter =  np.sqrt(xa *4 / np.pi)

    return diameter

A = np.array([[6.7, 1.3, 0.6, 0.7],
              [0.1, 5.5, 0.4, 2.4],
              [1.1, 0.8, 4.5, 1.7],
              [0.0, 1.5, 3.4, 7.5]])

b = np.array([1.1, 2.3, 3.3, 3.9])

#print colums 1 and 3 of A
print(A[:,[1,3]])

#print values of every entry in A that is greater than 2
print(A[A > 2])

#

def easy_reshape(obj, ncols, order = 'C'):
    '''
    guarantee that reshaping works by defining only one shape parameter
    '''

    #reshape
    arr = np.reshape(obj, (ncols, len(obj)/nocols), order)
    return arr
