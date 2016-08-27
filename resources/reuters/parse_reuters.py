#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from glob import glob


files = glob('reut2*.sgm')
outfile = 'reuters.txt'


with open(outfile,'wb') as output:
    for f in files:
        print f
        with open(f,'r') as fh:
            soup = BeautifulSoup(fh.read(),'lxml')
            for article in soup.findAll('reuters'):
                try:
                    topics = {x.text for x in article.find('topic').findAll('d')}
                    if 'earn' in topics:
                        continue
                except:
                    pass
                out_text = u'\n'.join([x for x in article.find('text').children if x.name is None])
                try:
                    output.write(out_text)
                except:
                    print out_text


