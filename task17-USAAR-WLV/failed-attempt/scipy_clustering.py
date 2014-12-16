#!/usr/bin/env python -*- coding: utf-8 -*-

from itertools import product

import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
import matplotlib.pylab as plt

from texeval import TexEval2015

nd = 2
texeval_corpus = TexEval2015()
sbcs = texeval_corpus.test_subcorpora
sbc = sbcs[nd]
terms = [i[1] for i in texeval_corpus.terms('test', sbc)]
numdomain = [i for i in range(1,8)]

methods = 'single complete average weighted'.split()
criterion = 'inconsistent distance maxclust'.split()
numclust = sorted([int(len(terms)/float(i)) for i in range(1,4)])

for me, cr, nc  in product(methods, criterion, numclust):
    terms = [i[1] for i in texeval_corpus.terms('test', sbc)]
    matrix = np.loadtxt(sbc+'.matrix')
    x = linkage(matrix, method=me)
    y = dendrogram(x)
    treename = "{}.{}.{}.png".format(me, cr, nc)
    plt.savefig('dendrograms/'+treename)
    z = fcluster(x,nc,cr)