import random
class Suben:
    def __init__(self,text,key):
        self.text = text
        self.key = key
        
class Encr(Suben):
    def __init__(self,text,key):
        Suben.__init__(self,text,key)
        self.e = ''
        for c in text :
            if ord(c) != 32:
                if ord(c) == 122 :
                    self.e += 'a'
                else :
                    self.e += chr(ord(c)+key)
            elif ord(c) == 32:
                self.e += ' '
    def display(self):
        return self.e
    
class Decr(Suben):
    def __init__(self,text,key):
        Suben.__init__(self,text,key)
        self.e = ''
        for c in text :
            if ord(c) != 32:
                if ord(c) == 122 :
                    self.e += 'a'
                else :
                    self.e += chr(ord(c)-key)
            elif ord(c) == 32:
                self.e += ' '
    def display(self):
        return self.e