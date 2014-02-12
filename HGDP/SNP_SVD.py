import numpy as np
import random as rand
import SNP_SVD_helpers as ml

# # computePvectForRows 
# 	Reads through the data and assigns values to the P vector for each row.
#
# 	parameters: > fname 	- string containing path to the dataset.
# 				> beta		- 0 < beta < 1 
# 	output:		- P 		- P is a vector with the i'th element corresponding
# 								to the probability weight of the i'th row.  
# 							  P = [p1, p2,..., pm]  
#								For all i pi>=0 and sum(P) = 1
# 	Assume that the data coming into this is formatted in a way that python 
#		recognizes and is able to parse correctly using the enumerate iterator.
#		This code also assumes the file includes both a header and row labels

def computePvectForRows(fname, beta=1, header=True, rowLabels=True) : 
	columns,rows = ml.data_size(fname)
	ARowMags = np.zeros([1,rows])
	for j,row in enumerate(fname) : 
		if j==0 and headder :
			pass 
		if headder : 
			j -= 1 			
		for i,value in enumerate(row) :
			if i==0 and rowLabels : 
				pass
			else : 
				ARowMags[0,j] += float(value)**2
	ARowMagsSum= ARowMags.sum() 
	P  =[  beta*ARowMags[0]/( ARowMagsSum ) ]
	return(P)


# # selectRowsForCmat 
# 	Takes in a vector of probabilities  (of length n) and randomly selects c ints 
#		in the domain [0,n] and returns them as an array C_sel. This function
#		 samples without replacement so no 2 values in C_sel should ever be equal
#		
# 	parameters: > P 	 	- P = [p1, p2,..., pm]  *P MUST BE A LIST NOT A NUMPY ARRAY*
#								For all i pi>=0 and sum(P) = 1
# 				> c			- the length of the desired output matrix
#				> seed 		- either a seed value for the randomization or None 
#								None -> teh randomization with use the time as a seed
# 	output:		- C_sel 	- Set of the indeces of the rows that were selected. 
#
# 	Assume that there are no negative probabilities and that sum(P)=1


def selectRowsForCmat( P , c , seed=None):
	Plen=P.__len__()
	C_sel=set()
	selected = 0
	while C_sel.__len__() < c :
		C_sel.add(ml.getRandomFromDist(P))
	return(C_sel)

def buildCfromA(fname, beta=1 , c) :
	P=computePvectForRows(fname, beta=1, header=True, rowLabels=True)
	C_sel = selectRowsForCmat(P, c)
	

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

	return H_k,V_e.transpose()

# I send Nate a list of row numbers that I want to put into C, he sends me C

def checkSVDvsEigDecomp(C, U_svd, S_svd, Vt_svd):
	S[:S_svd.__len__(), :S_svd.__len__()] = numpy.diag(S_svd)
	numpy.allclose(C, numpy.dot(U_svd, numpy.dot(S_svd, Vt_svd)))








