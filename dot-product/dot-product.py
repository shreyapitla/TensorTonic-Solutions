import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    # Write code here
    s=0
    if len(x)!=len(y):
        raise ValueError
    for i in range(0,len(x)):
        s+=x[i]*y[i]
    
        
    return s
    pass