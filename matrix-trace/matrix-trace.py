import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    A=np.array(A)
    rows,cols=A.shape
    trace=0
    if rows==cols:
        for i in range(0,rows):
            for j in range(0,cols):
                if i==j:
                    trace+=A[i][j]
    return trace
    
    pass
