# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 22:44:14 2020

@author: JonS
"""

from urllib import request
url = "http://www.gutenberg.org/files/2554/2554-0.txt"
response = request.urlopen(url)
raw = response.read().decode("utf-8-sig")


rtokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)
text.collocations()
html = request.urlopen(url).read().decode('utf8')

from bs4 import BeautifulSoup
import re
raw = BeautifulSoup(html, "lxml").get_text()
raw1a = sorted(set(w for w in nltk.corpus.nps_chat.raw()))
#1)  Exercise 1

raw1 = [w for w in raw if re.search('a-zA-Z]+', w)]
print(raw1) #returns empty list
nltk.re_show()

raw2 = [w for w in raw if re.search('[A-Z][a-z]*', w)]
print(raw2) #returns 25095 list of all upper case characters
nltk.re_show()

raw3 = [w for w in raw if re.search('p[aeiou]{,2}t', w)]
print(raw3) #empty list
nltk.re_show()

raw4 = [w for w in raw if re.search('\d+(\.\d+)?', w)]
print(raw4) #list of 209 terms, all numeric
nltk.re_show()

raw5 = [w for w in raw if re.search('([^aeiou][aeiou][^aeiou])*', w)]
print(raw5) #list of 1176966 terms, all single letter, mix of regular and special characters 'particularly back slash characters'
nltk.re_show()

raw6 = [w for w in raw if re.search('\w+|[^\w\s]+', w)]
print(raw6) #list of 943477 terms, all single letter, 
nltk.re_show()


#Exercise 2
#1)
re.findall(r"<a> <an> <the>",raw)

#2) 
stringlist = re.findall(r"T+h*", raw)  #*2 + 3



