#!/usr/bin/env python -*- coding: utf-8 -*-

import io, os
from itertools import chain

import numpy as np

def get_asiya_scores():
    indir = 'Asiya-outputs/'
    
    feature_data = {}
    for infile in os.listdir(indir):
        if infile in ['features.cp', 'features.sr', 'features.ne']:
            continue
        data = [[float(i) for i in line.strip().split()] 
                for line in io.open(indir+infile, 'r')]
        feature_data[infile] = data
    
    seventy_seven = [i + j + k + l for i,j,k, l in 
                     zip(feature_data['features.meteor'], 
                         feature_data['features.sp'], 
                         feature_data['features.ngram'], 
                         feature_data['features.esa']) if len(i+j+k+l) == 77]
    return seventy_seven


