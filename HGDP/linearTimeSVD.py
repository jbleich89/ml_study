
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

	index=-1
	if num==0:
		return 0
	else :
		index=-1
		while ( num > 0 ) :
			index+=1
			num  -= P[index]
		return index


# TODO: Need to go through and double check column vs rows
def linearTimeSVD( A , P , c , k ):
	Acols=cols(A)
	C=np.empty([c,Acols]) 
	if (not checkValidLinearTimeSVD(A , P , c , k)):
		return None
	for i in range(c):
		i_t = selectWitProb(P)
		beta = math.sqrt( c * P[i_t] )
		for j,val in enumerate(A[i_t,:]):
			C[i,j]=val/beta
	C_T=C.transpose()
	w, V = np.linalg.eig(C_T.dotC)
	
	H_k = n.empty([k,Acols])
	for i in range(k) : 
		h_t=C.dot(V[:,i])
		H_k[i,:]=h_t.divide(w[i])
	return H_k,V






