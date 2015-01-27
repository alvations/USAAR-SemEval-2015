#!/usr/bin/env python -*- coding: utf-8 -*-

from __future__ import unicode_literals

import io, sys, string
from itertools import chain
reload(sys); sys.setdefaultencoding("utf-8")

from nltk.corpus import wordnet as wn

from texeval import TexEval2015

texeval_corpus = TexEval2015()


for subcorpus in texeval_corpus.test_subcorpora:
    fout = io.open('single_outputs_leanless/'+subcorpus+'.taxo', 'w')
    terms = [term for termid, term in texeval_corpus.terms('test', subcorpus)]
    taxofile = 'taxo_outputs/knowledge-lean/rolling_cosine_taxo/' + subcorpus + '.taxo'
    
    taxo = {}
    for line in io.open(taxofile, 'r'):
        _, term, hypers = line.strip().split('\t')
        taxo[term] = hypers
    
    taxofile2 = 'taxo_outputs/knowledge-less/string_taxo/' + subcorpus + '.taxo'
        
    for line in io.open(taxofile2, 'r'):
        _, term, hypers = line.strip().split('\t')
        if term in taxo:
            taxo[term] = taxo[term]+','+hypers 
        else:
            taxo[term] = hypers
    
    domain = subcorpus[3:] if subcorpus.startswith('WN') else subcorpus
    
    dhyper = {'chemical':'substance', 'food':'substance', 
              'equipment':'device', 'science':'ability'}
    
    outline = "{}\t{}\t{}\n".format(0, domain, dhyper[domain])
    
    fout.write(outline)
    
    counter = 1
    for term in sorted(taxo):
        hypernyms = list(set([hyper for hyper in taxo[term].split(',') if hyper in terms]))
        for h in hypernyms:
            outline = "{}\t{}\t{}\n".format(counter, term, h)
            fout.write(outline.decode('utf8'))
            counter+=1
    