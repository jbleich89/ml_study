
import numpy as numpy
import random as rand

def rows(A):
	return len(A)
def cols(A):
	return A.size/len(A)

def checkValidLinearTimeSVD(A , P , c , k):
	Arows=rows(A)
	Acols=cols(A)
	valid = (1<=k and k<=c and c<=Acols)	
	valid = valid and (sum(P)==1)
	for i , p in enumerate(P) :
		valid = valid and p>=0	
	return valid

new=True
def selectWitProb(P) : 
	if new : 
		rand.seed(1)
		new = False
	num = rand.random()
	if num==0:
		return 0
	else :
		index=-1
		while ( num > 0 ) :
			index+=1
			num  -= P[index]
		return index

def data_size(fname, header=True, rowLabels=True):
    with open(fname) as f:
        for i, l in enumerate(f):
    		pass
    	for j, c in enumerate(l) : 
    		pass

	    if header : 
	    	rows = l
	    else :
	    	rows = l+1

	    if rowLabels : 
	    	columns = c 
	    else :
	    	columns = c+1
	    return columns , rows
	else :
		return None,None


def computePvectForRows(fname, beta, header=True, rowLabels=True) : 
	columns,rows = data_size(fname)
	ARowMags = np.zeros([1,rows])
	for j,row in enumerate(fname) : 
		if j==0 and headder :
			pass 
		if headder : 
			j -= 1 			
		for i,value in enumerate(row) :
			ARowMags[0,j] += float(value)**2
	ARowMagsSum= ARowMags.sum() 
	P  =[  beta*ARowMags[0]/( ARowMagsSum ) ]







# TODO: Need to go through and double check column vs rows
def SVD( P , C , k ):
	Ccols=cols(C)
	Crows=rows(C)	
	
	C_T=C.transpose()
	w_e, V_e = np.linalg.eig(C_T.dot(C))
	
	U_svd, S_svd, Vt_svd = np.linalg.svd(C, full_matrices=True)

	H_k = n.empty([k,Acols])
	for i in range(k) : 
		h_t=C.dot(V[:,i])
		H_k[i,:]=h_t.divide(w[i])
	return H_k,V

# I send Nate a list of row numbers that I want to put into C, he sends me C

def checkSVDvsEigDecomp(C, U_svd, S_svd, Vt_svd):
	S[:S_svd.__len__(), :S_svd.__len__()] = numpy.diag(S_svd)
	numpy.allclose(C, numpy.dot(U_svd, numpy.dot(S_svd, Vt_svd)))



