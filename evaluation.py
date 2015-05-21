from math import log, sqrt
import numpy as np

def  purity(groundtruthAssignment, algorithmAssignment):

    purity = 0  
    # Compute the purity
    cID = max(algorithmAssignment)+1
    gID = max(groundtruthAssignment)+1
    nk = [0]*cID
    kT =[0] * gID
    print "cID, gID", cID, gID
    print "kT_ini", kT 

    algorithmAssignment = np.asarray(algorithmAssignment)
    groundtruthAssignment = np.asarray(groundtruthAssignment)

    for i in range(cID):
        print "i" , i
        idK = np.where(algorithmAssignment == i)[0]
        #k_indices = np.asarray(k_indices)
        for j in range(gID):
            print "j" , j
            ngrand = np.where(groundtruthAssignment == j)[0]
            inter = set(idK) & set(ngrand)
            print "inter", len(inter)
            kT[j] = len(inter)
        print "kT", kT
        nk[i]=max(kT)
    print "nk", nk

    purity =1.0* np.sum(nk)/len(algorithmAssignment) 
    
    return purity 


def NMI(groundtruthAssignment, algorithmAssignment):

    NMI = 0
    # Compute the NMI
    cID = max(algorithmAssignment)+1
    gID = max(groundtruthAssignment)+1
    nData = len(algorithmAssignment)
    nTruth = len(groundtruthAssignment)
    pt = [0]*gID
    pc = [0]*cID
    pt_j = [0]*gID
    pc_i = [0]*cID
    pij = [[0]*cID for i in range(gID)]

    algorithmAssignment = np.asarray(algorithmAssignment)
    groundtruthAssignment = np.asarray(groundtruthAssignment)

    
    for i in range(cID):
        idK = np.where(algorithmAssignment == i)[0]
        p1 = 1.0*len(idK)/nData
        #print "idk ", idK
        #print "len(idK) ", len(idK)
      #  print "p1 ", p1
        if p1 != 0:
            pc[i] =  p1*log(p1)
        else:
            pc[i] = 0
        pc_i[i] = p1

    HC = -np.sum(pc)
    #print "HC", HC

    for j in range(gID):
        idT = np.where(groundtruthAssignment == j)[0]
        p2 = 1.0*len(idT)/nTruth
     #   print "p2 ", p2
        if p2 != 0:
            pt[j] = p2*log(p2)
        else:
            pt[j] =0
        pt_j[j] = p2

    HT = -np.sum(pt)
    #print "HT", HT

    for l in range(cID):
        idK = np.where(algorithmAssignment == l)[0]
        for ll in range(gID):
            ngrand = np.where(groundtruthAssignment == ll)[0]
            inter = set(idK) & set(ngrand)
     #       print " ngrand", ngrand
    #        print "idK", idK
            kT = 1.0*len(inter)/nData
      #      print "kT ", kT
            if (pc[l]*pt[ll]) != 0 and  kT !=0:
                pij[l][ll] = kT*log(kT/(pc_i[l]*pt_j[ll]))
            else:
                pij[l][ll]= 0
    Ict = np.sum(pij)
   # print "ICT",Ict
    
    NMI = Ict/sqrt(HC*HT)

    return NMI
