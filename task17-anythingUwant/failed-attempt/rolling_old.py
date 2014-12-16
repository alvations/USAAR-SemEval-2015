#!/usr/bin/env python -*- coding: utf-8 -*-

from __future__ import unicode_literals

import io, sys, string
from itertools import chain
reload(sys); sys.setdefaultencoding("utf-8")

import lucene
from java.io import File
# For Indexing.
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.document import Document, Field, FieldType
from org.apache.lucene.index import FieldInfo, IndexWriter, IndexWriterConfig
from org.apache.lucene.store import FSDirectory
from org.apache.lucene.util import Version
# For Querying.
from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.queryparser.classic import QueryParser
from org.apache.lucene.search import IndexSearcher

import numpy as np

from nltk.corpus import wordnet as wn
from nltk import sent_tokenize, word_tokenize

from gensim.utils import tokenize
from gensim.models import Word2Vec

from texeval import TexEval2015
from luluwiki import retrieve_wiki

texeval_corpus = TexEval2015()

wiki_index = '/home/alvas/engwiki/english-wiki'
lucene.initVM()

def filter_doc(term, doc):
    for i in sent_tokenize(doc):
        for j in i.split('\n'):
            if term.lower() in j.lower():
                yield j
            
def isa_doc(term, doc):
    for i in sent_tokenize(doc):
        if term+" is a" in i or "is a "+term in i or "is an "+term in i:
            yield i

def build_corpus_from_terms_with_wiki(sbc, searcher, analyzer):
    fout = io.open('WIKI_'+sbc, 'w', encoding='utf8')
    for termid, term in texeval_corpus.terms('test', sbc):
        docs = []
        for curl, doc in retrieve_wiki(term, searcher, analyzer):
            for fdoc in filter_doc(term, doc):
                docs.append(fdoc)
        
        print termid, term, len(docs)
        fout.write("{}\t{}\n".format(termid, term).decode('utf8'))
        for i in docs:
    
            fout.write(i.decode('utf8')+ '\n')
        fout.write('\n'.decode('utf8'))
    return sbc

def build_corpus(n=0):
    sbcs = texeval_corpus.test_subcorpora
    sbc = sbcs[n]
    # Hack for parallelizing queries, uses one index per domain.
    directory = FSDirectory.open(File(wiki_index+'-'+sbc))
    searcher = IndexSearcher(DirectoryReader.open(directory))
    analyzer = StandardAnalyzer(Version.LUCENE_CURRENT)
    build_corpus_from_terms_with_wiki(sbc, searcher, analyzer)

def build_word_vector(n=0, mincount=1):
    sbcs = texeval_corpus.test_subcorpora
    sbc = sbcs[n]
    corpus_name = 'WIKI_'+sbc
    sentences = []
    current_term = ""
    with io.open(corpus_name, 'r', encoding='utf8') as fin:
        for line in fin:
            if '\t' in line:
                current_term = line.strip().split('\t')[1]
            if line.strip().endswith('.'):
                if current_term in line:
                    # Single tokenize terms.
                    depunct_term = "".join(['_' if ch in string.punctuation or 
                                            ch == ' ' else ch 
                                            for ch in current_term])
                    line.replace(current_term, depunct_term)
                sentences.append(list(tokenize(line)))
    model = Word2Vec(sentences, size=100, window=5, 
                     min_count=mincount, workers=2, iter=10)
    model.save(corpus_name+'.10epochs.singletok.min'+str(mincount)+'.deep')

def test_vector(n=0, mincount=1):
    sbcs = texeval_corpus.test_subcorpora
    sbc = sbcs[n]
    fname = 'WIKI_'+'.10epochs.singletok.min'+str(mincount)+'.deep'
    model = Word2Vec.load(fname)
    
    for termid, term in texeval_corpus.terms('test', sbc):
        if len(term.split()) == 1 and term in model:
            print termid, term, model[term]
            

def get_matrix(n=0):
    sbcs = texeval_corpus.test_subcorpora
    sbc = sbcs[n]
    fname = 'WIKI_'+sbc+'.100epochs.phrasal.singletok.min1.deep'
    model = Word2Vec.load(fname)
    
    terms = [i[1] for i in texeval_corpus.terms('test', sbc)]
    matrix_lol = [[0 for x in range(len(terms))] for x in range(len(terms))]
     
    for termid1, term1 in enumerate(terms):
        for termid2, term2 in enumerate(terms):
            term1 = "".join(['_' if ch in string.punctuation or ch == ' ' 
                             else ch for ch in term1])
            term2 = "".join(['_' if ch in string.punctuation or ch == ' ' 
                             else ch for ch in term2])
            print term1, term2, termid1, termid2, len(matrix_lol), len(terms)
            try:
                similarity = model.n_similarity(term1, term2)
                distance = 2*(1-similarity)
            except:
                distance = 1
            matrix_lol[termid1][termid2] = distance
    matrix = np.array(matrix_lol)
    np.savetxt(sbc+'.matrix', matrix)
    

def build_taxo(n=0):
    pass
    # Parse cluster for hypernyms.
    # Output to file.

def main(domain_number, mincount=1):
    #build_word_vector(int(domain_number), int(mincount))
    get_matrix(int(domain_number))
    

if __name__ == '__main__':
  import sys
  main(*sys.argv[1:])
