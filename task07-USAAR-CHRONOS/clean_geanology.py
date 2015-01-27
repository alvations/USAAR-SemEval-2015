#!/usr/bin/python -*- coding: utf-8 -*-


import os, io, json
import HTMLParser
from BeautifulSoup import BeautifulSoup as bsoup

indir = '/home/alvas/daikon/freepages.genealogy.rootsweb.ancestry.com/_dutillieul/ZOtherPapers/'

read = []
miss = []
for i in os.listdir(indir):
    if not i.endswith('html'):
        continue
    with io.open(indir+i, 'r', encoding='utf8') as fin:
        try:
            fin.read()
            read.append(i)
        except:
            miss.append(i)

print len(read), len(miss)