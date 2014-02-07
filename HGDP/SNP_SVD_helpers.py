
import numpy as numpy
import random as rand
import sys


# # rows
#	Takes in an array of arrays and returns the number of rows in the matrix
#
# 	parameters: > A 	 	- a 2D array or numpy matrix
# 	output:		- rows  	- the number of rows in A

def rows(A):
	return A.__len__()

# # cols
#	Takes in an array of arrays and returns the number of cols in the matrix
#
# 	parameters: > A 	 	- a 2D array or numpy matrix
# 	output:		- cols  	- the number of rows in A

def cols(A):
	return A[0].__len__()

# # data_size
#	Takes in the name of a file that contains a 2D matrix of data and returns the size
#		of that 2D array of data
#
# 	parameters:	> fname 	- string containing path to the data.
#				> header 	- boolean value.
#								True when the first line of data has a header
#				> rowLabels	- boolean value.
#								True when the first elements in a given row is a row label
#	
# 	output:		- cols 		- the number of columns in the data
#				- rows 		- the number of rows in the data

# NOTES! no empty rows allowed in the text file. File must be formatted well
# to be tested

def data_size(fname,delim=' ', header=True, rowLabels=True):
	with open(fname,'r') as f:
		try: 
			lines = 0
			i=0
			for line in (f):
				lines+=1
				if (not header and lines==2) : 
					l=line.split(delim)
					i=len(l)
				elif (lines==1) :
					l=line.split(delim)
					i=len(l)
				else :
					pass

			if header:
				rows = lines-1
			else :
				rows = lines
			if rowLabels : 
				cols = i -1
			else :
				cols = i
			return cols , rows
		except IOError as e:
			print  "I/O error({0}): {1}".format(e.errno, e.strerror)
			return 
		except:
			print "Unexpected error:", sys.exc_info()[0]
			raise 


# # getRandomFromDist
# 	Takes in a vector of probabilities  (of length n) and randomly selects one index 
#		in the domain [0,n] and returns it
#		
# 	parameters: > P 	 	- P = [p1, p2,..., pm]  *P MUST BE A LIST NOT A NUMPY ARRAY*
#								For all i pi>=0 and sum(P) = 1
#				> seed 		- either a seed value for the randomization or None 
#								None -> teh randomization with use the time as a seed
# 	output:		- index 	- index of the selected row
#
# 	Assume that there are no negative probabilities and that sum(P)=1
#		Bad things happen if sum(P)!=1


def getRandomFromDist(P,seed=None):
	if seed !=None: 
		rand.seed(seed)
	num = rand.random()
	if num==0:
		return 0
	else :
		index=-1
		while ( num > 0 )  :
			index+=1
			num  -= P[index]
		return index

