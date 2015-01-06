#!/usr/bin/env python -*- coding: utf-8 -*-

import io, urllib, urllib2, string, re, time, HTMLParser
from BeautifulSoup import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


fout = io.open("chronoeval.final", 'w')

def get_spectator_date(url):
    try:
        date = url.split('/')[-3]
        year = date[-4:]
        return year, date
    except:
        search_result = urllib2.urlopen(url).read()
        bsoup2 = BeautifulSoup(search_result)
        for bs in bsoup2.findAll('div'):
            if bs.get('class') == 'date':
                date = bs.text.split('Page')[0]
                year = date.split()[-1].strip(',')
                return year, date
        
def get_genealogy_year(url):
    date = url.rpartition('/')[2].split('.')[0]
    year = url[-9:-5]
    
    if date == "FordingtonMarriages1766-1812Part2":
        year = "1766"
    if date == "8thJanuary1842B":
        year = "1842"
    
    return year, date

with io.open('chronoeval.output', 'r') as fin1, io.open('chrono-patch', 'r') as fin2:
    for line in fin1:
        line = line.strip().split('\t')
        if len(line) == 3:
            id, url, date = line
            date = date.split('-')[0]
            year = date.split()[-1]
            assert int(year) and len(year) == 4
            outline = "{}\t{}\t{}\t{}\n".format(id, year, url, date).decode('utf8')
            fout.write(outline)
            
    for line in fin2:
        line = line.strip().split('\t')
        if len(line) == 2 and '|||' not in line[1]:
            id, url = line
            if 'spectator.co.uk' in url:
                year, date = get_spectator_date(url)
                assert int(year) and len(year) == 4 
                fout.write("{}\t{}\t{}\t{}\n".format(id, year, url, date).decode('utf8'))
            else:
                year, date = get_genealogy_year(url)
                assert int(year) and len(year) == 4
                fout.write("{}\t{}\t{}\t{}\n".format(id, year, url, date).decode('utf8'))
                
        if len(line) == 3 and '|||' not in line[1] and line[0] != '#':
            id, year, url = line
            date = "UNKNOWN"
            assert int(year) and len(year) == 4
            fout.write("{}\t{}\t{}\t{}\n".format(id, year, url, date).decode('utf8'))