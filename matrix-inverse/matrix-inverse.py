import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    # Write code here
    A=np.array(A)
    if(A.ndim==2 and A.shape[0]==A.shape[1]):
        if(np.linalg.det(A)==0):
            return None
        else:
            return np.linalg.inv(A)
    else:
        return None
    pass
