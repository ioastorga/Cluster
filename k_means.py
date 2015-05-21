from utils import *
import numpy as np


def computeSSE(data, centers, clusterID):
    sse = 0 
    nData = len(data) 
    for i in range(nData):
        c = clusterID[i]
        sse += squaredDistance(data[i], centers[c]) 
        
    return sse 

def updateClusterID(data, centers):
    nData = len(data) 
    nCenters = len(centers)
    clusterID = [0] * nData
    DisToCenter = [0] * nCenters

    # assign the closet center to each data point
    for i in range(nData):
        #print "i ", i
        for j in range(nCenters):
            DisToCenter[j] = np.sqrt(squaredDistance(data[i], centers[j]))
        clusterID[i] = DisToCenter.index(min(DisToCenter))
    #print"clusterID", clusterID
    return clusterID

# K: number of clusters 
def updateCenters(data, clusterID, K):
    nDim = len(data[0])
    centers = [[0] * nDim for i in range(K)]
    #print "len centers in kmeans = ", len(centers)
    
    # Recompute the centers based on current clustering assignment
    # If a cluster doesn't have any data points, in this homework, leave it to ALL 0s
    
    clusterIDarr = np.asarray(clusterID)
    data_Arr = np.asarray(data)
    for j in range(K):
        k_indices = np.where(clusterIDarr == j)[0]
   #     print "k ", j
    #    print "indices for  k", k_indices
        if len(k_indices)==0:
            centers[j] = [0] * nDim
        else:
          #  print "type data ", type(data)
           
            centers[j] = np.sum(data_Arr[k_indices], axis=0)/len(k_indices)
  #  print "centers after loop ",centers[j]
    return centers 

def kmeans(data, centers, maxIter = 100, tol = 1e-6):
    nData = len(data) 
    
    if nData == 0:
        return [];

    K = len(centers) 

    clusterID = [0] * nData
    
    if K >= nData:
        for i in range(nData):
            clusterID[i] = i
        return clusterID

    nDim = len(data[0]) 
    
    lastDistance = 1e100
    
    for iter in range(maxIter):
#        print "iter " , iter
        clusterID = updateClusterID(data, centers) 
        centers = updateCenters(data, clusterID, K)
        
        curDistance = computeSSE(data, centers, clusterID) 
        if lastDistance - curDistance < tol or (lastDistance - curDistance)/lastDistance < tol:
            print "# of iterations:", iter 
            print "SSE = ", curDistance
            return clusterID
        
        lastDistance = curDistance
        
    print "# of iterations:", iter 
    print "SSE = ", curDistance
    return clusterID


