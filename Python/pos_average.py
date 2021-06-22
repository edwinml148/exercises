# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 11:04:06 2021

@author: USER
"""

def comparacion ( s1 , s2 ):
    cont = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if ( i == j and s1[i] == s2[j] ):
                cont = cont + 1
    
    return cont

def pos_average(s1):
    conta_f = 0
    x = 0
    s = list( s1.split(", ") )
    #print(s)
    tem = len(s[0])
    while ( len(s) > 1 ):
        
        temp = s[0]
        s.pop(0)
        cont = 0
        for j in s:
            x = x + 1

            cont  = cont + comparacion(temp,j)

        conta_f = conta_f + cont 

        
    return  round((100.0*conta_f)/(x*tem), 10)
                  

# Link Kata : https://www.codewars.com/kata/59f4a0acbee84576800000af/train/python

