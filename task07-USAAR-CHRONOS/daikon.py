#!/usr/bin/python -*- coding: utf-8 -*-

import os, io, json
import HTMLParser
from BeautifulSoup import BeautifulSoup as bsoup

#import sys; reload(sys); sys.setdefaultencoding('utf8')

unescape = HTMLParser.HTMLParser().unescape

indir = '/home/alvas/daikon/spectator-dump/'
fout = io.open('daikon-spectator.json', 'w', encoding='utf8')
titles = []


fout.write(u'[')
for i in os.listdir(indir):
    data = {}
    url = 'http://archive.spectator.co.uk'+i.replace('_', '/')
    try:
        x = io.open(indir+i, 'r', encoding='utf8')
        soup = bsoup(unicode(x.read()))
    except UnicodeError as e:
        print i, e
        
    title, date, _ = [unicode(unescape(i.strip())) for i in 
                      soup.find('title').text.split('&raquo;')]
    if title in titles:
        continue
    
    titles.append(title)
    text = [unicode(unescape(paragraph.text)) for paragraph in soup.findAll('p') 
            if paragraph.get('class') == 'body']
            
            
    data['url'] = url
    data['title'] = title
    data['date'] = date
    data['body'] = text
    
    
    
    out_json = json.dumps(data, indent=2, ensure_ascii=False)
    fout.write(out_json+u',\n')
    
fout.write(u']')    