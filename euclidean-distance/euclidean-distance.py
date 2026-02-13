import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    X=np.array(x)
    Y=np.array(y)
    sums=np.sum((X-Y)**2)
    ans=np.sqrt(sums)
    return ans
    pass