import numpy as numpy


def rows(A):
	return len(A)
def cols(A):
	return A.size/len(A)

def checkValidLinearTimeSVD(A , P , c , k):
	Arows=rows(A)
	Acols=cols(A)
	value = (1<=k and k<=c and c<=Acols)
	value = ()


def linearTimeSVD( A , P , c , k ):
	valid = checkValidLinearTimeSVD(A , P , c , k)


U, s, V = np.linalg.svd(C)


