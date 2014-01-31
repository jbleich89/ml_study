import csv,sys,numpy
from collections import Counter

filename='./hgdp_truncated_data/HGDP_first1000_justSNPs_as_Numbers.csv'

# To be substituted later for a better dictionary mapping
# See:	Numerical Representation of DNA Sequences Based on 
#		Genetic Code Context and Its Applications in Periodicity 
#		Analysis of Genomes

genDict= {	'AA'	:	11,\
			'AC' 	:	12,\
			'AG' 	:	13,\
			'AT' 	:	14,\
			'CA'	:	21,\
			'CC' 	:	22,\
			'CG' 	:	23,\
			'CT' 	:	24,\
			'GA'	:	31,\
			'GC' 	:	32,\
			'GG' 	:	33,\
			'GT' 	:	34,\
			'TA'	:	41,\
			'TC' 	:	42,\
			'TG' 	:	43,\
			'TT' 	:	44 }

def modes(values):
	count = Counter(values)
	for v in values:
		count[v]+=1
	best = max(count.values())
	ans=  [k for k,v in count.items() if v == best]
	if ans.__len__()>0:
		# print ans[0]
		return ans
	else :
		return None



SNPlen=1043
SNParr = [None]*1045
with open(filename,'rb') as csvfile:
	HGDPreader=csv.reader(csvfile, delimiter=',')
	try :
		for row in HGDPreader:
			mostCommon=modes(row);
			for i,val in enumerate(row):
				if val=='--':
					row[i] = mostCommon

			# print row
	except csv.Error as e :
		sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
