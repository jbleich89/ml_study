import csv,sys
from collections import Counter
import numpy as np
import numpy.ma as ma
LTE=False


filenameLTE='HGDP_FinalReport_Forward_header_and_first_1000.txt'
filenameFull='./HGDP_FinalReport_Forward.txt'

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
	print count.items()
	if ans.__len__()>0:
		# print ans[0]
		return count.items
	else :
		return None
import itertools
import operator

def most_common(L):
  # get an iterable of (item, iterable) pairs
  SL = sorted((x, i) for i, x in enumerate(L))
  # print 'SL:', SL
  groups = itertools.groupby(SL, key=operator.itemgetter(0))
  # auxiliary function to get "quality" for an item
  def _auxfun(g):
    item, iterable = g
    count = 0
    min_index = len(L)
    for _, where in iterable:
      count += 1
      min_index = min(min_index, where)
    # print 'item %r, count %r, minind %r' % (item, count, min_index)
    return count, -min_index
  # pick the highest-count/earliest item
  return max(groups, key=_auxfun)[0]
def letters(allels):
	mode = most_common(allels)[0]
	letters =[]
	for allel in allels:
		if allel[0] != '--':
			for letter in range(2):
				letters.append(allel[0][letter])
	letters = sorted(set(letters))
	b1b1 = letters[0] + letters[0]   	# +1
	b1b2 = []    #If there is only one letter they remain -1
	b2b1 = []
	if len(letters) == 2:
		b1b2 = letters[0] + letters[1]   #  0    ###CHECK THAT SINGLE LETTER LOGIC WORKS
		b2b1 = letters[1] + letters[0]   #  0
		b2b2 = letters[1] + letters[1]   # -1
		if mode == b1b1:
			allels = {b1b1 : 0 , b1b2 : 1 , b2b1 : 1  , b2b2 : -1 , '--' : mode}
		elif mode == b1b2:
			allels = {b1b1 : 1 , b1b2 : 0 , b2b1 : 0  , b2b2 : -1 , '--' : mode}
		elif mode == b2b1:
			allels = {b1b1 : 1 , b1b2 : 0 , b2b1 : 0  , b2b2 : -1 , '--' : mode}
		elif mode == b2b2:
			allels = {b1b1 : 1 , b1b2 : -1 , b2b1 : -1  , b2b2 : 0 , '--' : mode}
		return allels
	return {b1b1 : 0 , '--' : 0	}	
def check_missing(values):
	count = Counter(values)
	for v in values:
		count[v]+=1
	best = max(count.values())
	allels = count.most_common()[:3:1]	 
	allels = letters (allels)	
	c= count ['--']
	s= sum(count.values())
	if float(c)/float(s) >=.1:
		return np.nan, allels
	else:
		return values, allels	
def substitue_allels(row):
	row , allels_dict = check_missing(row)
	try:
		if np.isnan(row):
			return -2
	except:
		for element in range(len(row)):
			for i in allels_dict:
				if i == row[element]:
					row[element] = allels_dict[i]
		return np.array(row)
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
# def probability(row, frobenius):
# 	spectral, frobenius = norms(row)
# 	p = spectral^2/frobenius^2
# 	return p




SNPsamples=1043

csv.register_dialect('HGDPreader', delimiter='\t', skipinitialspace=True, strict=True)
# SNPlen=file_len(filename)
# SNPname = [None]*SNPlen
# spectral_norm = [None]*SNPlen
# SNPmat= np.empty([SNPlen, SNPsamples])


with open(filename,'rb') as csvfile:
	#	for line in csvfile:	
	HGDPreader=csv.reader(csvfile, 'HGDPreader')
	Subjects_header=HGDPreader.next()
	row =  ' '.join(map(str, Subjects_header))
	with open("clean_data.txt", "a") as myfile:
		myfile.write(row + '\n')
	cnt = 0
	try :
		# for i in range(90000):
		# 	HGDPreader.next()
		for row in HGDPreader:
			
			cnt += 1 
			# if cnt == 10000:
			# 	break
			#SNPname[cnt] = row[0]
			header = row[0]
			if cnt % 5000 == 0:
				print cnt
			try:
				row = substitue_allels(row[1:])
			except:
				print 'There was an error'
				print cnt
				row =  ' '.join(map(str, row))
				with open("error_log.txt", "a") as myfile:
	   				myfile.write(row + '\n')
			try:
				if row == -2:
					continue
			#SNPmat[cnt]=row
			except:
				row =  ' '.join(map(str, row))
				with open("clean_data.txt", "a") as myfile:
	   				myfile.write(header + ' ' + row + '\n')
	except csv.Error as e :
		sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))

