# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 10:29:35 2017
test
@author: tmahas
"""

import xml
import xml.etree.cElementTree as cet

tree = cet.parse('enwiki-test2.xml')

root = tree.getroot()

"""
The text is placed in a structure like this
<page>
    <revision>
        <text>
            ...text...
        <\text>
    <\revision>
<\page<

"""    

dictio = {}
pageno = 1
    
for child in root:
    for child2 in child:
        if child2.tag.lower() == 'revision':
            for child3 in child2:
                if child3.tag.lower() == 'text':
                    if str(child3.text)[0:9] != '#REDIRECT':
                        text_str = str(child3.text)
                        dictio[pageno] = (text_str)
                        pageno += 1
                        
                        
""" Iterative with iterparse() """

import xml
import xml.etree.cElementTree as cet

open('wiki.txt', 'w').close()

"xmlfile = 'enwiki-test2.xml'"
xmlfile = 'enwiki-20170820-pages-articles.xml'

for event, elem in cet.iterparse(xmlfile):
    if elem.tag == '{http://www.mediawiki.org/xml/export-0.10/}text':
        if str(elem.text)[0:9] != '#REDIRECT':
            text_str = str(elem.text).encode("ascii", errors="ignore").decode()
            text_str = text_str.replace('\n', " ")
            "dictio[pageno] = (text_str)"
            with open("wiki.txt", "a") as wiki_file:
                wiki_file.write(text_str+'\n')
    elem.clear()
    
    
import re

""""""""""""""""""""""""""""""""
""" Insert your pattern here """

pattern = 'euclid[a-z]+'

""""""""""""""""""""""""""""""""

wiki = open("wiki.txt", "r")
regex = re.compile(pattern)
words = set({})

for line in wiki:
    result = regex.findall(line)
    "for entry in result:"
    "    print(entry)"
    words = words.union(set(result))
print(words)

""""""""""""""""""""""""""""""""


  

       


                

        

        





