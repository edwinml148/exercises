# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def order(sentence):
    words = sentence.split(" ")
    ind = []
    dicci = []
    for i in words:
        for j in i:
            try:
                ind.append(int(j))
                dicci.append( (int(j),i) )
            except ValueError:
                pass

    lst_sorted = sorted(dicci, key = lambda x: x[0])
    string_final = ''
    
    w = list ( map(lambda x: x[1] , lst_sorted) )     
    return " ".join(w)


# link kata : https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python


