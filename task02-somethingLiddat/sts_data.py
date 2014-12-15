#!/usr/bin/env python -*- coding: utf-8 -*-

import io, os,re

import sys; reload(sys); sys.setdefaultencoding("utf-8")

STS2012_TEST = {'STS.input.MSRpar.txt': 'STS.gs.MSRpar.txt',
                'STS.input.MSRvid.txt':'STS.gs.MSRvid.txt', 
                'STS.input.surprise.SMTnews.txt': 'STS.gs.surprise.SMTnews.txt',
                'STS.input.SMTeuroparl.txt':'STS.gs.SMTeuroparl.txt',
                'STS.input.surprise.OnWN.txt': 'STS.gs.surprise.OnWN.txt'}

STS2012_TRAIN = {'STS.input.MSRpar.txt':'STS.gs.MSRpar.txt',
                 'STS.input.SMTeuroparl.txt':'STS.gs.SMTeuroparl.txt',
                 'STS.input.MSRvid.txt':'STS.gs.MSRvid.txt'}

STS2013_GOLD = {'STS.input.SMT.txt':'STS.gs.SMT.txt', 
                'STS.input.OnWN.txt':'STS.gs.OnWN.txt',
                'STS.input.headlines.txt':'STS.gs.headlines.txt',
                'STS.input.FNWN.txt':'STS.gs.FNWN.txt'}

STS2014_GOLD = {'STS.input.deft-news.txt': 'STS.gs.deft-news.txt', 
                'STS.input.images.txt':'STS.gs.images.txt',
                'STS.input.deft-forum.txt':'STS.gs.deft-forum.txt',
                'STS.input.OnWN.txt':'STS.gs.OnWN.txt',
                'STS.input.headlines.txt': 'STS.gs.headlines.txt',
                'STS.input.tweet-news.txt': 'STS.gs.tweet-news.txt'}

STS_DATA_DIR = 'STS-data/'
STS_DATA = {'STS2012-train/':STS2012_TRAIN,'STS2012-test/':STS2012_TEST,
            'STS2013-gold/':STS2013_GOLD, 'STS2014-gold/':STS2014_GOLD}


def create_dot_all_file():
    fout1 = io.open('left.all', 'w')
    fout2 = io.open('right.all', 'w')
    fout3 = io.open('score.all', 'w')
    
    for dataset in STS_DATA:
        for inputfile, goldstandard in STS_DATA[dataset].iteritems():
            inputfile = STS_DATA_DIR + dataset + inputfile
            goldstandard = STS_DATA_DIR + dataset + goldstandard
            with io.open(inputfile, 'r') as infile, io.open(goldstandard, 'r') as goldfile:
                line_counter = 0
                for line, score in zip(infile, goldfile):
                    ##docid = inputfile + '_' + str(line_counter)
                    ##docid = docid.replace('.', '_').replace('/', '_').replace('-', '_')
                    #line_counter+=1
                    left, right = line.strip().split('\t')
                    score = score.strip()
                    fout1.write(left+'\n')
                    fout2.write(right+'\n')
                    fout3.write(score+'\n')

def create_meteor_output_all_file():
    cmd = 'java -Xmx2G -jar meteor-1.5/meteor-*.jar left.all right.all > meteor.output.all'
    os.system(cmd)

def create_metor_out_file():
    with io.open('meteor.output.all', 'r') as fin, io.open('meteor.all', 'w') as fout:
        for i in re.findall(r'Segment [0-9].* score\:.*\n', fin.read()):
            fout.write(i.strip().split()[-1] + '\n')

def get_meteor_scores():
    with io.open('meteor.output.all', 'r') as fin:
        meteor_scores = [float(i.strip().split()[-1]) for 
                               i in re.findall(r'Segment [0-9].* score\:.*\n', 
                                               fin.read())]
        return meteor_scores

def get_sts_scores():
    with io.open('score.all', 'r') as fin:
        sts_scores = [float(i) for i in fin]
        return sts_scores
    



create_metor_out_file()










