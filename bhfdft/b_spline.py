import numpy as np

def augknt(knots, order):
    array = np.zeros(len(knots)+2*(order-1))
    array[:order-1] = knots[0]
    array[order-1:-order+1] = knots
    array[-order+1:] = knots[-1]
    return array
