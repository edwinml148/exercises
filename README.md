# Codewars Exercises

Solutions of exercises that I have done throughout my career as a developer. I hope it helps you and don't hesitate to leave me a feedback!

* [Stop gninnipS My sdroW! ( 6 Kyu )](#1)
* [Bit Counting ( 6 Kyu )](#2)

##  1. Stop gninnipS My sdroW! ( 6 Kyu )

Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (like the name of this kata).

Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.

Link Kata : https://www.codewars.com/kata/5264d2b162488dc400000001/train/python

```
def spin_words(sentence):
    
    def reversa(word):
        if( len(word) >= 5 ):
            return word[len(word)::-1]
        else:
            return word
    
    words = list(map(reversa,sentence.split(" "))) 
    
    
    
    return " ".join(words)
```

##  2. Bit Counting ( 6 Kyu )

Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Link Kata : https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python

```
def count_bits(n):
    bin = []
    while( n//2 >= 2 ):
        bin.append(n%2)
        n = n//2
        #print(n)
    
    bin.append(n%2)
    bin.append(n//2)
    
    cont = 0
    for i in bin:
        if(i == 1):
            cont = cont +1
    
    #print(cont)
    return cont
```
