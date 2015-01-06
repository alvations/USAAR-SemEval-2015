#!/usr/bin/env python -*- coding: utf-8 -*-

import io, urllib, urllib2, string, re, time, HTMLParser
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 
                             os.pardir))
reload(sys)
sys.setdefaultencoding("utf-8")

from BeautifulSoup import BeautifulSoup

from pybing import Bing

def get_date(htmlfile, option):
    """
    >>> get_date('archivedotspectator.html', 'spectator')
    28 APRIL 1849, Page 10
    >>> get_date('newspaperdotcom.html', 'newspaper')
    Saturday, December 11, 1897
    """
    if option == 'spectator':
        with io.open(htmlfile, 'r') as fin:
            bsoup = BeautifulSoup(fin.read())
            return bsoup.find('div', id="article").find('div').text
    elif option == 'newspaper':
        with io.open(htmlfile, 'r') as fin:
            bsoup = BeautifulSoup(fin.read())
            return bsoup.find('dd', itemprop="date datePublished").text

class SemEval2015Task17:
    def __init__(self):
        self.test_task1 = '../semeval2015-data/test_task7/testT1.txt'
        self.test_task2 = '../semeval2015-data/test_task7/testT2.txt'
        self.test_task3 = '../semeval2015-data/test_task7/testT3.txt'


def bing(content_html):
    pass

fout = io.open('chronoeval.output', 'w', encoding='utf8')
chronoeval = SemEval2015Task17()

with io.open(chronoeval.test_task1, 'r', encoding='utf8') as fin:
    bsoup = BeautifulSoup(fin.read())
    for text in bsoup.findAll('text'):
        id = text.get('id')
        old_content = " ".join(text.text.decode('utf8').split()[:30])
        content = "".join([ch for ch in str(old_content) if ch not in string.punctuation])
        archive_url = 'http://archive.spectator.co.uk/search?term='
        content_html = urllib.quote_plus(content)
        search_result = urllib2.urlopen(archive_url + content_html).read()
        
        archive_domain = 'http://archive.spectator.co.uk/'
        
        bsoup2 = BeautifulSoup(search_result)
        
        try:
            first_result = bsoup2.find('div', id='results').find('a').get('href')
            first_result = archive_domain + first_result
            
            first_result_date = [i.text for i in 
                                 bsoup2.find('div', id='results').findAll('span') 
                                 if i.get('class') == 'date'][0]
            outline = "{}\t{}\t{}\n".format(id, first_result, 
                                            first_result_date).decode('utf8')          
            fout.write(outline)
            print outline 
        except:
            content_html = urllib.quote_plus(content)
            try:
                search_result = urllib2.urlopen('http://www.bing.com/search?q=' + content_html).read()
            except:
                time.sleep(5)
                search_result = urllib2.urlopen('http://www.bing.com/search?q=' + content_html).read()
            genealogy_regx = r'http:\/\/freepages\.genealogy\.rootsweb\.ancestry\.com\/.*'
            if 'freepages.genealogy.rootsweb.ancestry.com/' in search_result:
                first_result = re.findall(genealogy_regx, search_result)[0].split('"')[0]
                first_result = HTMLParser.HTMLParser().unescape(first_result)
                page = urllib2.urlopen(first_result).read()
                print id, first_result
                
                '''
                try:
                    first_result_date = re.findall(r'<B>.*\, .*, [0-9].*\.', page)[0][3:]
                except:
                    first_result_date =  " ".join([i for i in 
                                          re.findall(r'<B>.*<\/B>', page)])

                outline = "{}\t{}\t{}\n".format(id, first_result, 
                                            first_result_date).decode('utf8')
                fout.write(outline)
                print outline
                '''
            else:
                ##print search_result
                outline = "{} ||| {} ||| {}\n".format(id, 'http://www.bing.com/search?q=' + content_html, archive_url + content_html).decode('utf8')
                fout.write(outline)
                print outline
                