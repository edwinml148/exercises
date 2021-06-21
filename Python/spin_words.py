def spin_words(sentence):
    
    def reversa(word):
        if( len(word) >= 5 ):
            return word[len(word)::-1]
        else:
            return word
    
    words = list(map(reversa,sentence.split(" "))) 
    
    
    
    return " ".join(words)


# Link Kata : https://www.codewars.com/kata/5264d2b162488dc400000001/train/python