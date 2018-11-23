import random
def sub(text,key=0):
    e = ''
    for c in text :
        if ord(c) != 32:
            if ord(c) == 122 :
                e += 'a'
            else :
                e += chr(ord(c)+key)
        elif ord(c) == 32:
            e += ' '
    return e
#a = 'The chick is crazy'
#e = sub(a,1)
#print(a)
#print(e)