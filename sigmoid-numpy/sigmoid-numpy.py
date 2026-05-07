import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    if(type(x)==list):
        x1=np.asarray(x,dtype=float)
        x1=np.asarray(list(map((lambda k:1/(1+np.exp(-k))),x1)),dtype=float)
        return x1
    else:
        return 1/(1+np.exp(-x))
    pass