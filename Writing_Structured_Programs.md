##Structured Programming Week 2

1)
```

#Exercise 1

#list
words = ['is', 'NLP', 'fun', '?']

#translate to '[NLP is fun !]

tmp = words[0]
words[0] = words[1]
words[1] = tmp
words[3] = '!'
print(words)

#tuple
words = ('is', 'NLP', 'fun', '?')
#words = list(words)

tmp4 = '!'
newwords = (words[1], words[0], words[2], tmp4)
print(newwords)
#translate to '[NLP is fun !]
```

#Exercise 2
```
n = 5
m = 10
word_table = [['']*n]*m

word_table[1][2] = "hello"

```

#Exercise 3

```
text = 'I am sam sam I am I do not like green eggs and ham'
def shorten(text, n):
    
    
    for i in range(n):
        textlist = text.split(" ")
        n =len(textlist)
        hist1=dict(zip(list(textlist),[list(textlist).count(i) for i in list(textlist)]))
    
        K, L = max((K, L) for L, K in hist1.items())
                
        textlist = list(filter(lambda a: a != L, textlist))
       
        newtext = ""
        for s in textlist:
            newtext = newtext + ' ' + s
        text = newtext
    return text
    
test = shorten(text, 2)

print(test)

"""
 am am do not like green eggs and ham
 
 Removed 'I' and 'sam' from example text string when removing the 2 most common words
 
 """


```

 #Exercise 4
 
 ```
text = 'I am sam sam I am I do not like green eggs and ham add more things about green eggs and ham sam eggs and ham newwordexample'
 
def novel10(text):
     
    textlist = text.split(" ")
    n = len(textlist)
    n4 = int(n/10)
   
    n2 = n - n4
    checklist = textlist[:n2]
    newlist = textlist[n2:]
    printlist = []
    for i in range(n4):
        for j in range(n2):
            if newlist[i] == checklist[j]:
                printlist.append(newlist[i])
    newtext = ""
    for s in printlist:
        newtext = newtext + ' ' + s
    return newtext
    
test1 = novel10(text)
print(test1)                
        
"""
Prints "Ham" in the above example.

"""    
```    