import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    V=np.array(v)
    cols=V.shape[0]
    A=np.zeros((cols,cols))
    for i in range(0,cols):
        A[i][i]=V[i]
    return A
    pass
