#!/usr/bin/env python -*- coding: utf-8 -*-

import random, itertools
from collections import defaultdict
random.seed(0)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.image import grid_to_graph
from sklearn.cluster import AgglomerativeClustering

from texeval import TexEval2015
texeval_corpus = TexEval2015()

n=2
sbcs = texeval_corpus.test_subcorpora
sbc = sbcs[n] 
print sbc
terms = [row[1] for row in texeval_corpus.terms('test', sbc)]

matrix = np.loadtxt(sbc+'.matrix')

n_clusters = int(len(terms)/float(3))
model = AgglomerativeClustering(n_clusters=n_clusters,
                                linkage="ward", affinity="euclidean")
model.fit(matrix)

ii = itertools.count(matrix.shape[0])
nodes = [{'node_id': next(ii), 'left': x[0], 'right':x[1]} for x in model.children_]

nodes_to_hypernyms = defaultdict(list)

for i in nodes:
    right = i['right']
    left = i['left']
    hypernym = i['node_id']
    nodes_to_hypernyms[right] = hypernym
    nodes_to_hypernyms[left] = hypernym
    
    
# Get clusters.
for term, clusterid in zip(terms, model.labels_):
    hypernym_chain = []
    while nodes_to_hypernyms[clusterid]:
        hypernym_chain.append(nodes_to_hypernyms[clusterid])
    print clusterid, term, hypernym_chain

#print n_clusters, len(terms)
#print model.n_components_
#print model.n_leaves_
#print len(model.children_)
#print model.children_

#for row in model.children_:
#print row

'''
for row in model.children_:
    if int(row[0]) > l or int(row[1]) > l:
        print row
    else:
            
        try:
            t1 = terms[row[0]]
            t2 = terms[row[1]]
            print row, t1, " ||| ", t2
        except:
            continue
'''

'''
print n_clusters, len(terms), min(model.labels_), max(model.labels_)


# Get clusters.
for term, clusterid in zip(terms, model.labels_):
    print clusterid, term
'''


'''
for l in np.arange(model.n_clusters):
    for row in model.labels_ == l:
        print row
    #print matrix[model.labels_ == l].T
    break
''' 

'''
plt.figure()
for l, c in zip(np.arange(model.n_clusters), 'rgbk'):
    plt.plot(matrix[model.labels_ == l].T, c=c, alpha=.5)
plt.show()
'''