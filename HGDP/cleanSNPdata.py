import csv,sys,numpy
from collections import Counter

LTE=True


filenameLTE='./hgdp_truncated_data/HGDP_FinalReport_Forward_short.txt'
filenameFull='./hgdp_truncated_data/HGDP_FinalReport_Forward.txt'

if LTE:
	filename=filenameLTE
else : 
	filename=filenameFull

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
		return ans[0]
	else :
		return None


SNPsamples=1043
SNP_LTE_len=100
SNPlen=660918

csv.register_dialect('HGDPreader', delimiter='\t', skipinitialspace=True, strict=True)

with open(filename,'rb') as csvfile:
	HGDPreader=csv.reader(csvfile, 'HGDPreader')
	Subjects_headder=HGDPreader.next()
	if LTE:
		SNPmat= [[None]*SNPsamples for index in range(SNP_LTE_len)]
	else :
		SNPmat= [[None]*SNPsamples for index in range(SNPlen )]
	try :
		cnt=-1
		for row in HGDPreader:
			cnt+=1
			mostCommon=modes(row);
			for i,val in enumerate(row[1:row.__len__()]):
				if val=='--':
					row[i] = mostCommon
				print i 
				print cnt
				SNPmat[cnt][i-1]=row[i]
	except csv.Error as e :
		sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
