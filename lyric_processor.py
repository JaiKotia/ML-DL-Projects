#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 19:08:09 2018

@author: jai
"""
#Libraries
import billboard
import pandas as pd
import numpy as np
from musixmatch import Musixmatch
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import pos_tag
from textblob.classifiers import NaiveBayesClassifier

nltk.download()

musixmatch = Musixmatch('0420fc6e8cc2586e23222f0d8a968df3')

#Initialization

training_set=[]
test_set=[]

chart_names=['adult-contemporary', 'greatest-hot-latin-songs',
             'rap-song', 'rock-songs',
             'country-songs','r-and-b-songs', 'greatest-country-songs']

chart = billboard.ChartData(chart_names[6])
table = pd.DataFrame()
songs=[]
artists=[]
all_lyrics=""
lyrics=""

#Get Song Details

i=0
while(i<100):
    artists.append(chart[i].artist)
    i+=1
        

i=0
while(i<100):
    songs.append(chart[i].title)
    i+=1    
    
table['Title']=pd.Series(songs)    
table['Artist']=pd.Series(artists)


#Get Song Lyrics

i=0
while(i<100):
    lyrics=((((musixmatch.matcher_lyrics_get(table['Title'][i], table['Artist'][i]).get('message')).get('body')).get('lyrics')).get('lyrics_body'))
    all_lyrics+=lyrics.split('...', 1)[0]
    i+=1


all_lyrics=all_lyrics.replace(',', '')

#Text Processing
processed_lyrics=all_lyrics.split("\n")
processed_lyrics=list(filter(None, processed_lyrics))

i=0
while(i!=len(processed_lyrics)):
    processed_lyrics[i]+="', 'country'"
    i+=1


processed_lyrics = ["'" + line for line in processed_lyrics]
processed_lyrics=[tuple(x.replace('\'', '').split(',')) for x in processed_lyrics]

print(processed_lyrics)


#Training Data
training_set+=processed_lyrics

print(training_set)

#Testing Data

test_set+=processed_lyrics
print(test_set)


#Sentiment Analysis

analyser = SentimentIntensityAnalyzer()    
def print_sentiment_scores(sentence):
    snt = analyser.polarity_scores(sentence)
    print("{:-<40} {}".format(sentence, str(snt)))
    
print(analyser.polarity_scores(lyrics))    

for line in processed_lyrics:
    print_sentiment_scores(line)
        
print_sentiment_scores(lyrics)

#Pos Tagging
pos_check=lyrics.split(" ")

pos = []

for line in processed_lyrics:
    pos.append(pos_tag(line))
    
    
print(pos_tag(processed_lyrics))    


#Naive Bayes Classifier

cl = NaiveBayesClassifier(training_set)

cl.classify("Just let it go")
cl.classify("Nigga's be hatin on me")
cl.classify("I gotta feeling, that tonight will be a good night")
cl.classify("Hey Jude, don't be afraid")

cl.accuracy(test_set)


genre_classifier = NaiveBayesClassifier(training_set)

genre_classifier.accuracy(test_set)

genre_classifier.classify("Bet your window's rolled down and your hair's pulled back And I bet you got no idea you're going way too fast You're trying not to think about what went wrong Trying not to stop 'til you get where you goin'You're trying to stay awake so I bet you turn on the radio and the song goes")

 