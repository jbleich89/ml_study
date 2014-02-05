import csv,sys,numpy
from collections import Counter

LTE=True


filenameLTE='./hgdp_truncated_data/HGDP_FinalReport_Forward_short.txt'
filenameFull='./hgdp_truncated_data/HGDP_FinalReport_Forward.txt'

if LTE:
	filename=filenameLTE
else : 
	filename=filenameFull

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


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

csv.register_dialect('HGDPreader', delimiter='\t', skipinitialspace=True, strict=True)

with open(filename,'rb') as csvfile:

	SNPlen=file_len(filename)

	SNPmat= [[None]*SNPsamples for index in range(SNPlen)]
	
	HGDPreader=csv.reader(csvfile, 'HGDPreader')
	
	Subjects_headder=HGDPreader.next()
	
	try :
		cnt=-1
		for row in HGDPreader:
			cnt+=1
			mostCommon=modes(row);
			SNPlen
			for i,val in enumerate(row[1:row.__len__()]):
				if val==B1B1:
					row[i] = '1'
				else if val==B1B2 or val=B2B1 : 
					row[i] = '0'
				else if val==B2B2 : 
					row[i] = '-1'
				SNPmat[cnt][i]=row[i]
				# TODO: eliminate SNP's with more than 10% missing values.
	except csv.Error as e :
		sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
