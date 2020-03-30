##NLP Week 2

The assignment was to build unigrams and bigrams of two corpuses, and compare word frequncies. I misread the initial assignment,
and also added in a smoothed version of each of the models.

Overall, both documents were similar. The term 'xyz' was zero for unigram and bigram models, including smoothed models.
This is because the term 'xyz' does not exist in the corpus, so adding one to the numerator during the maximum likelihood estimator process,
does not prevent the probabilitiy of that word from being zero. The most notable difference in the two corpuses, 'brown' and 'stopwords'
is that brown is a much bigger corpus, and seems to have a wider range of non-zero probabilities under the non-smoothed model. 

Code is below:
```

#Unigram Models
from nltk.corpus import brown
from collections import Counter

total_count = len(brown.words())
print(total_count)
print()

counts = Counter(brown.words())
for item in counts:
    print(item)
print(counts['the']) #the number of times 'the' appears
print()

#20 most common words
most_common = counts.most_common(n=20)
for word, value in most_common:
    print(word, value)
print()
V = len(counts)
# frequencies
"""Smoothed Version """
for word in counts:
    counts[word] = (counts[word]+1) / (float(total_count) + V)

print(counts['the']) # 'the': 0.051521093876437773
print(counts['xyz']) # 0
print(counts['books']) #7.640178796614333e-05

"""Non-Smoothed version """

for word in counts:
    counts[word] /= float(total_count)

print(counts['the']) # 0.05400743374050114
print(counts['xyz']) # 0
print(counts['books']) # 7.922893027165189e-05
sorted(counts)


from nltk.corpus import stopwords
from collections import Counter

total_count = len(brown.words())
print(total_count)
print()

counts = Counter(brown.words())
for item in counts:
    print(item)
print(counts['the']) #the number of times 'the' appears
print()

#20 most common words
most_common = counts.most_common(n=20)
for word, value in most_common:
    print(word, value)
print()
V = len(counts)
# frequencies
"""Smoothed Version """
for word in counts:
    counts[word] = (counts[word]+1) / (float(total_count) + V)

print(counts['the']) 
print(counts['xyz']) 
print(counts['books']) 

"""Non-Smoothed version """

for word in counts:
    counts[word] /= float(total_count)

print(counts['the']) 
print(counts['xyz']) 
print(counts['books']) 
sorted(counts)

"""

BIGRAM MODELS


"""

from nltk.corpus import brown
from collections import Counter


from nltk import bigrams

first_sentence = brown.sents()[0]
list(bigrams(first_sentence, pad_left=True, pad_right=True))


from collections import defaultdict
counts = defaultdict(lambda: defaultdict(int))
#get regular, unsmoothed count, also get word length

for sentence in brown.sents():
    for w1, w2 in bigrams(sentence, pad_right=True, pad_left=True):
        counts[w1][w2] += 1

V = len(counts)

"""smoothed count """
for w1 in counts:
    total_count = float(sum(counts[w1].values()))
    for w2 in counts[w1]:
        counts[w1][w2] =  (counts[w1][w2] + 1) / (total_count + V)
print(counts["the"]["books"]) # 0.00011787
print (counts["the"]["xyz"]) # 0.0
print(counts[None]["The"]) # 0.057717

"""Non-smoothed count """
for w1 in counts:
    total_count = float(sum(counts[w1].values()))
    for w2 in counts[w1]:
        counts[w1][w2] =  (counts[w1][w2]) / (total_count)

print(counts["the"]["books"]) # 0.00020729354360332874
print (counts["the"]["xyz"]) # 0.0
print(counts[None]["The"]) # 0.161543241465

"""
There are differences when examining the brown corpus. One thing to note, is that xyz does not appear to be in the corpus,
so even adding a 1 to the numerator in order to create non-zero probabilities will not do this for new words. For the other
word combinations tried, the smoothed version has lower probabilities for each bigram tried.
"""

from nltk.corpus import stopwords
from collections import Counter


from nltk import bigrams

first_sentence = brown.sents()[0]
list(bigrams(first_sentence, pad_left=True, pad_right=True))


from collections import defaultdict
counts = defaultdict(lambda: defaultdict(int))
#get regular, unsmoothed count, also get word length

for sentence in brown.sents():
    for w1, w2 in bigrams(sentence, pad_right=True, pad_left=True):
        counts[w1][w2] += 1

V = len(counts)

"""smoothed count """
for w1 in counts:
    total_count = float(sum(counts[w1].values()))
    for w2 in counts[w1]:
        counts[w1][w2] =  (counts[w1][w2] + 1) / (total_count + V)
print(counts["the"]["books"]) # .0001178
print (counts["the"]["xyz"]) # 0.00
print(counts[None]["The"]) # .057717

"""Non-smoothed count """
for w1 in counts:
    total_count = float(sum(counts[w1].values()))
    for w2 in counts[w1]:
        counts[w1][w2] =  (counts[w1][w2]) / (total_count)

print(counts["the"]["books"]) #.00018
print (counts["the"]["xyz"]) #0.0
print(counts[None]["The"]) #.10296

```
