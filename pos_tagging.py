#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 17:34:19 2018

@author: jai
"""

import nltk  
nltk.download() 


noise_list = ["is", "a", ",", "..."] 
def _remove_noise(input_text):
    words = input_text.split() 
    noise_free_words = [word for word in words if word not in noise_list] 
    noise_free_text = " ".join(noise_free_words) 
    return noise_free_text

with open('text.txt') as fd:
    data=fd.read()

_remove_noise(data)

import re 

def _remove_regex(input_text, regex_pattern):
    urls = re.finditer(regex_pattern, input_text) 
    for i in urls: 
        input_text = re.sub(i.group().strip(), '', input_text)
    return input_text

regex_pattern1 = ",[\w]*"
regex_pattern2 = ".[\w]*"  

_remove_regex(data, regex_pattern1)
_remove_regex(data, regex_pattern2)

from nltk import word_tokenize, pos_tag

tokens = word_tokenize(data)

print (pos_tag(tokens))
