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
    
    return cont
        
##
# Link Kata : https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python

