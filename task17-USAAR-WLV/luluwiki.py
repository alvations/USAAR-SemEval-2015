#!/usr/bin/env python -*- coding: utf-8 -*-

import io, sys, os, lucene, threading, time
from datetime import datetime

import lucene

from java.io import File
# For Indexing.
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.document import Document, Field, FieldType
from org.apache.lucene.index import FieldInfo, IndexWriter, IndexWriterConfig
from org.apache.lucene.store import FSDirectory
from org.apache.lucene.util import Version
# For Querying.
from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.queryparser.classic import QueryParser
from org.apache.lucene.search import IndexSearcher

def wikicorpusxml(xmlfile):
    """ 
    Iterates through the xml file document by document
    
    USAGE:
    
    for xmldoc in wikicorpusxml('test.xml'):
    #print xmldoc
    content = xmldoc.partition('>')[2].partition('<')[0].strip()
    print content
    print '###'
    """
    with io.open(xmlfile, 'r', encoding='utf8') as fin:
        doc = []
        for line in fin:
            # Skips empty lines
            if not line.strip(): continue
            # When document ends
            if line.endswith('</doc>\n'):
                doc.append(line.strip())
                yield "\n".join(doc)
                doc = []
            else:
                doc.append(line.strip())

def index_wiki(wiki_xmlfile, index_directory_name):
    # Initialize index directory and analyzer.
    version = Version.LUCENE_CURRENT
    store = FSDirectory.open(File(index_directory_name))
    analyzer = StandardAnalyzer(version)
    # Creates config file.
    config = IndexWriterConfig(version, analyzer)
    config.setOpenMode(IndexWriterConfig.OpenMode.CREATE)
    writer = IndexWriter(store, config)
    # Set document content field type.
    content_fieldtype = FieldType()
    content_fieldtype.setIndexed(True)
    content_fieldtype.setStored(True)
    content_fieldtype.setTokenized(True)
    content_fieldtype.setIndexOptions(FieldInfo.IndexOptions.DOCS_AND_FREQS_AND_POSITIONS)
    
    # Set document title field type.
    title_fieldtype = FieldType()
    title_fieldtype.setIndexed(True)
    title_fieldtype.setStored(True)
    title_fieldtype.setTokenized(True)
    title_fieldtype.setIndexOptions(FieldInfo.IndexOptions.DOCS_AND_FREQS_AND_POSITIONS)
    
    # Set document url field type.
    url_fieldtype = FieldType()
    url_fieldtype.setIndexed(True)
    url_fieldtype.setStored(True)
    url_fieldtype.setTokenized(False)
    url_fieldtype.setIndexOptions(FieldInfo.IndexOptions.DOCS_AND_FREQS_AND_POSITIONS)
    
    
    for xmldoc in wikicorpusxml((wiki_xmlfile)):
        content = xmldoc.partition('>')[2].partition('<')[0].strip()
        title = xmldoc.partition(' title="')[2].partition('"')[0].strip()
        url = xmldoc.partition(' url="')[2].partition('"')[0].strip()
        doc = Document()
        doc.add(Field("contents", content, content_fieldtype))
        doc.add(Field("title", title, title_fieldtype))
        doc.add(Field("url", url, url_fieldtype))
        writer.addDocument(doc)
     
    writer.commit()
    writer.close()

def retrieve_wiki(text_query, searcher, analyzer):    
    txt =text_query
    try:
        query = QueryParser(Version.LUCENE_CURRENT, "contents", 
                            analyzer).parse(txt)
    except:
        qp = QueryParser(Version.LUCENE_CURRENT, "contents", analyzer)
        txt = qp.escape(txt)
        query = qp.parse(txt)
    scoreDocs = searcher.search(query, 1000).scoreDocs
    
    for scoreDoc in scoreDocs:
        doc = searcher.doc(scoreDoc.doc)
        yield doc.get('title'), doc.get('contents')    

'''
ind_dir = '/home/alvas/english-wiki'
wikixml = 'test.xml'
lucene.initVM()
for title, i in retrieve_wiki('Eiffel', ind_dir): 
    print i
    print '######'
'''