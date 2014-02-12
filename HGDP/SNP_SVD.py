import numpy as np
import random as rand
import SNP_SVD_helpers as ml
import csv
from matplotlib import pyplot as plt
import pylab
from mpl_toolkits.mplot3d import Axes3D

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

def computePvectForRows(fname, beta=1):#, header=True, rowLabels=True) : 
	columns,rows = ml.data_size(fname)
	ARowMags = [0]*rows
	P = [0]*rows
	with open(fname,'rb') as f : 
		reader=csv.reader(f,delimiter=' ')
		for j,row in enumerate(reader) : 
			if j!=0 : 
				# print(j)
				j -= 1 	
				for i,value in enumerate(row) :
					if i!=0: 
						ARowMags[j] += float(value)**2
	# print(ARowMags)
	ARowMagsSum= sum(ARowMags) 
	for k in range(rows):
		P[k]=  beta*ARowMags[k]/( ARowMagsSum ) 
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
	# Plen=P.__len__()
	C_sel=set()
	selected = 0
	while C_sel.__len__() < c :
		C_sel.add(ml.getRandomFromDist(P))
	return(C_sel)



def buildCfromA(fname, c, beta=1 ) :
	cols,rows= ml.data_size(fname)
	P=computePvectForRows(fname, beta=1)#, header=True, rowLabels=True)
	# print(P)
	C_sel = selectRowsForCmat(P, c)
	# print(C_sel)
	C=np.zeros([c,cols])
	with open(fname,'rb') as f : 
		reader=csv.reader(f,delimiter=' ')
		cnt=0
		for j,row in enumerate(reader) : 
			# print(row)
			if j==0 :
				pass 
			elif j-1 in C_sel :
				# print(C[cnt,:])
				# print(row[1:]) 
				C[cnt,:]=(row[1:])
				cnt+=1
		return(C)


# TODO: Need to go through and double check column vs rows
def SVD( C , k ):
	Ccols=ml.cols(C)
	C_T=np.transpose(C)
	# w_e, V_e = np.linalg.eig(C_T.dot(C))	
	U_svd, S_svd, Vt_svd = np.linalg.svd(C, full_matrices=True)
	Ht_svd = np.transpose(U_svd)[:k,:]
	# print(Ht_svd)
	Projected = Ht_svd.dot(C)
	return Projected

# def checkSVDvsEigDecomp(C, U_svd, S_svd, Vt_svd):
# 	S[:S_svd.__len__(), :S_svd.__len__()] = numpy.diag(S_svd)
# 	numpy.allclose(C, numpy.dot(U_svd, numpy.dot(S_svd, Vt_svd)))

def SVDSNP( c, 	fname='../hgdp_truncated_data/clean_data.txt', dimensions=3):
	C=buildCfromA(fname, c)
	res = SVD(C,dimensions)
	return res

def SNP_main(c=950):
	res1=SVDSNP(250)
	res2=SVDSNP(500)
	res3=SVDSNP(750)
	res4=SVDSNP(900)
	fig = pylab.figure()
	ax1 = fig.add_subplot(2, 2, 1, projection='3d')
	ax1.scatter(res1[0,:],res1[1,:],res1[2,:])
	ax2 = fig.add_subplot(2, 2, 2, projection='3d')
	ax2.scatter(res2[0,:],res2[1,:],res2[2,:])
	ax3 = fig.add_subplot(2, 2, 3, projection='3d')
	ax3.scatter(res3[0,:],res3[1,:],res3[2,:])
	ax4 = fig.add_subplot(2, 2, 4, projection='3d')
	ax4.scatter(res4[0,:],res4[1,:],res4[2,:])
	plt.show()

if __name__=="__main__":
	SNP_main()






