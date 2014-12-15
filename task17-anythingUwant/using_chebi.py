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



def read_chebi():
    termid_to_name = defaultdict(list)
    name_to_termid = {}
    termid_to_hypernyms = defaultdict(list)
    with io.open('chebi.obo', 'r') as fin:
        for term in per_section(fin):
            if not term.startswith('[Term]'): continue
            else:
                termid, names, hypernyms = [], [], []
                for line in term.split('\n'):
                    # CHEBI term ID
                    if line.startswith('id'): 
                        termid = line.strip()[4:]
                    # Inventory name
                    if line.startswith('name'): 
                        names.append(line.strip()[6:].lower())
                    # Synonyms name
                    if line.startswith('synonym') and line.strip().endswith('RELATED [ChEBI:]'):
                        synonym = line.strip()[9:].lower()
                        synonym = synonym.rpartition('"')[0].strip('"')
                        names.append(synonym)
                    # Hypernyms
                    if line.startswith('is_a'): 
                        hypernyms.append(line.strip()[6:])    
            
            termid_to_name[termid] = names
            for name in names:
                name_to_termid[name] = termid
            termid_to_hypernyms[termid] =  hypernyms
            #print termid, name, hypernyms
            
    return name_to_termid, termid_to_name, termid_to_hypernyms

def generate_taxo_from_chebi(subcorpus='chemical', dateset='test'):
    """
    USAGE: 
    >>> for i,j in generate_taxo_from_chebi('chemical').iteritems():
    >>>     print i,j
    >>>     break
    epivoacorine 2-methylmaleyl,citraconoyl group,citraconoyl
    """
    term_to_hypernyms = {}
    # Read the chebi.obo file.
    chebi_terms, chebi_termids, chebi_isa = read_chebi() 
    # A list of chemicals in chemical.terms but not in CHEBI
    not_in_chebi = [u'chemical', u'galactsose', 
                    u'n-acylhexadecaphytosphinganine', 
                    u'n-acylhexosylsphingosine', u'monophosphate', 
                    u'fluorobenzene', u'l-erythro-n-acyl-sphingosine', 
                    u'benzoylecgonine', u'ioxitalamic acid', u'triphosphate', 
                    u'thifensulfuron methyl', u'tetraphosphate', 
                    u'bisphosphate', u'o-phosphorylhomoserine']
    wnterms_not_in_chebi = []
    for termid, term in texeval_corpus.terms('test', subcorpus):
        if term not in chebi_terms:
            wnterms_not_in_chebi.append(term)
            continue
        if term in not_in_chebi:
            continue
        else:
            hypernyms = list(set(chain(*[chebi_termids[hypernym] for hypernym in 
                                         chebi_isa[chebi_terms[term]]])))
            term_to_hypernyms[term] = ",".join(hypernyms)

    print len(wnterms_not_in_chebi)
    return term_to_hypernyms
