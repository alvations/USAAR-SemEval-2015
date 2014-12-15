#!/usr/bin/env python -*- coding: utf-8 -*-

import io, os

import sys; reload(sys); sys.setdefaultencoding("utf-8")

print os.listdir('STS-data/STS2013-gold')

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

STS_DATA = {'STS2012-TRAIN':STS2012_TRAIN,'STS2012-TEST':STS2012_TEST,
            'STS2013-GOLD':STS2013_GOLD, 'STS2014-GOLD':STS2014_GOLD}


