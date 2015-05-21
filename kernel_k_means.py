from utils import * 
from math import exp 

def kernel(data, sigma):
    nData = len(data)
    Gram = [[0] * nData for i in range(nData)] 
    
    # Calculate the Gram matrix 
    for i in range(nData):
        xi = data[i]
        for j in range(nData):
            xj = data[j]
            sdis = squaredDistance(xi,xj)
            Gram[i][j] = exp(-sdis/(2.0*sigma*sigma))
    return Gram 


