#!/usr/bin/env python -*- coding: utf-8 -*-

from __future__ import unicode_literals

import io
import sys; reload(sys); sys.setdefaultencoding("utf-8")

from using_chebi import generate_taxo_from_chebi
from using_sumo import generate_taxo_from_sumo
from using_stringdist import generate_taxonomy_from_within

from texeval import TexEval2015
texeval_corpus = TexEval2015()

subcorpora = texeval_corpus.test_subcorpora



for subcorpus in subcorpora:
    '''
    fout = io.open('sumo_taxo/'+subcorpus+'.taxo', 'w')
    sumo_taxo = generate_taxo_from_sumo(subcorpus)
    for i,term_hypernym in enumerate(sumo_taxo.iteritems()):
        term, hypernym = term_hypernym
        outline = '{}\t{}\t{}\n'.format(i, term, hypernym).decode('utf8')
        fout.write(unicode(outline))
    '''
        
    if 'chemical' in subcorpus:
        fout = io.open('chebi_taxo/'+subcorpus+'.taxo', 'w')
        chebi_taxo = generate_taxo_from_chebi(subcorpus)
        for i,term_hypernym in enumerate(chebi_taxo.iteritems()):
            term, hypernym = term_hypernym
            outline = '{}\t{}\t{}\n'.format(i, term, hypernym).decode('utf8')
            fout.write(unicode(outline))

    '''
    fout = io.open('string_taxo/'+subcorpus+'.taxo', 'w')
    string_taxo = generate_taxonomy_from_within(subcorpus)
    for i,term_hypernym in enumerate(string_taxo.iteritems()):
        term, hypernym = term_hypernym
        outline = '{}\t{}\t{}\n'.format(i, term, hypernym).decode('utf8')
        fout.write(unicode(outline))
    '''