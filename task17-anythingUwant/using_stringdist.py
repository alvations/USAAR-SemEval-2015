#!/usr/bin/env python -*- coding: utf-8 -*-

from __future__ import unicode_literals

import io, sys, string
from collections import defaultdict
from itertools import chain
reload(sys); sys.setdefaultencoding("utf-8")

from nltk.corpus import wordnet as wn

from util import per_section
from texeval import TexEval2015
texeval_corpus = TexEval2015()

def generate_taxonomy_from_within(subcorpus, dateset='test'):
    """
    USAGE:
    >>> for i,j in generate_taxonomy_from_within('science').iteritems():
    >>>    print i,j
    >>>    break
    astronomy and astrophysics physics
    """
    term_to_hypernyms = {}
    terms = [term for termid, term in texeval_corpus.terms('test', subcorpus)]
    
    for t1 in terms:
        hypernyms = [t2 for t2 in terms if t1 != t2 and len(t1)>3 and t2 in t1]
        if hypernyms:
            term_to_hypernyms[t1] = ",".join(hypernyms)
        
    return term_to_hypernyms




