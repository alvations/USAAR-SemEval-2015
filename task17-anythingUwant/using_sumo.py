#!/usr/bin/env python -*- coding: utf-8 -*-

from __future__ import unicode_literals

import io, sys, string
from itertools import chain
reload(sys); sys.setdefaultencoding("utf-8")

from nltk.corpus import wordnet as wn

from texeval import TexEval2015

texeval_corpus = TexEval2015()

def generate_taxo_from_sumo(subcorpus, dateset='test', option='first_sense'):
    """
    Options:
    - first_synset (i.e. lemma_names from only the first synset)
    - all_synsets (i.e. lemma_names from all synset)
 
    USAGE:
    >>> for i,j in generate_taxo_from_sumo('WN_science').iteritems():
    >>>     print i,j
    >>>     break
    mammalogy zoology,zoological science
    >>> for i,j in generate_taxo_from_sumo('science', option='all_senses').iteritems():
    >>>     print i,j
    >>>     break
    social science science,scientific discipline
    """
    term_to_hypernyms = {}
    for termid, term in texeval_corpus.terms(dateset, subcorpus):
        term_synsets = wn.synsets(term.replace(' ', '_'), pos='n')
        if option == 'first_sense':
            # Check if first synset and hypernyms exists
            try: term_hypernyms = term_synsets[0].hypernyms()
            except: continue
            # Retrieves lemma_names of hypernyms.
            hypernyms = list(set(chain(*[hypernym.lemma_names()
                                         for hypernym in term_hypernyms])))
            lemma_names = [lemma.replace('_', ' ') for lemma in 
                           hypernyms if lemma]
            term_to_hypernyms[term] = ",".join(lemma_names)
        elif option == 'all_senses':
            hypernyms = list(set(chain(*[synset.hypernyms() 
                                         for synset in term_synsets])))
            if hypernyms:
                lemma_names = list(set(chain(*[hypernym.lemma_names()
                                               for hypernym in hypernyms])))
                lemma_names = [lemma.replace('_', ' ') for lemma in lemma_names
                               if lemma]
                term_to_hypernyms[term] = ",".join(lemma_names)
    return term_to_hypernyms