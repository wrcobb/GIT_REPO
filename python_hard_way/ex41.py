# -*- coding: utf-8 -*-
"""
Created on Sat May 23 00:24:08 2015

@author: wrcobb
"""

import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):" :
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" :
        "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)" :
        "class %%% has-a function named *** that takes self and @@@ parameters."      
,
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

#do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == 'english':
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False
    
#load up the words from the website:
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())
    
