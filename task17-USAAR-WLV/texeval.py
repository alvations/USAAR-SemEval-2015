#!/usr/bin/env python -*- coding: utf-8 -*-

import io, os

#from natsort import natsorted

class TexEval2015:
    def __init__(self):
        self.texeval_trial_dir = 'TExEval_trialdata_1.2'
        self.texeval_test_dir = 'TexEval_testdata_1'
        self.texeval_tool_dir = 'TExEval_tool_1.0'
        self.trial_subcorpora = ['ontolearn_AI', 'WN_plants', 'WN_vehicles']
        self.test_subcorpora = ['chemical', 'equipment', 'food', 'science', 
                                'WN_chemical', 'WN_equipment', 'WN_food', 
                                'WN_science']
    
    def terms(self, trial_test, subcorpus):
        """
        Input terms.
        
        >>> teval = TexEval2015()
        >>> for termid, term in teval.terms('ontolearn_AI'):
        ...     print termid, term
        """
        indir = self.get_directory_path(trial_test)
        termfile = os.path.join(indir, subcorpus+'.terms')
        for i in io.open(termfile, 'r'):
            termid, term = i.strip().split('\t')
            yield int(termid), term 
    
    def taxo(self, trial_test,  subcorpus):
        """
        Gold ontology.
        
        >>> teval = TexEval2015()
        >>> for relid, term, hypernym in teval.taxo('trial', 'onotlearn_AI'):
        ...     print relid, term, hypernym
        """
        indir = self.get_directory_path(trial_test)
        taxofile = os.path.join(indir, subcorpus+'.taxo')
        for i in io.open(taxofile, 'r'):
            relid, term, hypernym = i.strip().split('\t')
            yield int(relid), term, hypernym
    
    def taxoeval(self, trial_test, subcorpus):
        """
        Human evaluation
        
        >>> teval = TexEval2015()
        >>> for relid, right in teval.taxoeval('trial', 'ontolearn_AI'):
        ...     print relid, right
        """
        indir = self.get_directory_path(trial_test)
        ansfile = os.path.join(indir, subcorpus+'.taxo.eval')
        for i in io.open(ansfile, 'r'):
            relid, right = i.split('\t')
            right = True if right.strip() else False
            yield int(relid), right
    
    def get_directory_path(self, trial_test):
        if trial_test == 'trial':
            return self.texeval_trial_dir
        elif trial_test == 'test':
            return self.texeval_test_dir