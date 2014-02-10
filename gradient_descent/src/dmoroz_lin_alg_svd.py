# goal is to implement http://cs-www.cs.yale.edu/homes/mmahoney/pubs/matrix2_SICOMP.pdf page 166
import math, random, numpy

def LinearTimeSVD(A, c, k, P):
    C = numpy.empty([m,c])
    sumprob = 0
    for p_i in P:
        sumprob += p_i
    if sumprob != 1:
        print("probs don't add up")

    for t in range(1,c):
        i_t, p_i_t = generateRandRow(c,P)
        C[t] = A[i_t] / sqrt(t*p_i_t)

    ctc = c.dot(c.transpose())
    w,v = numpy.linalg.eig(ctc)


def generateRandRow(P):
    #random.seed(1)
    sumprob = 0
    nextRand = random.random()
    for i, p_i in enumerate(P):
        sumprob += p_i
        if sumprob >= nextRand:
            return i, p_i