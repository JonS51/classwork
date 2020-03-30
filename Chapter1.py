# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 21:07:40 2020

@author: JonS
"""
import nltk
#from nltk.book import *


#exercise 1

from nltk.corpus import brown
V = set(text2)
brownwords =  [w for w in V if len(w) > 10]

f_brownwords = FreqDist(sorted(brownwords))
               
    
f_brownwords #gives the frequency distribution of the words with > 10 characters



#2) Gives a printed list of all upper case words for monty python and the holy grail.
def if_uppercase(text):
    text1 = text
    upper_list = []
    for s in text1:
        capitalcount = s.istitle()
        if capitalcount == True:
            upper_list.append(s)
    return(upper_list)

montypythonwords = if_uppercase(text6)
montypythonwords  # Gives list of words with capital letters in them. 



def percent1(word, text):
    wordcount = int(text.count(word))
    words = int(len(text))
    perc = float(wordcount / words)
    return(perc)
    
    
# 3) gives the percentage of times a word is used in a given text
text = text2
word = 'the'
p_check = percent1(word, text)
print("{0:0%}".format(p_check))

