class Mirror:
    def __init__(self,text):
        self.text = text
    def text_revmirror(self):
        words = self.text.split()
        text_rev1 = " ".join(reversed(words))
        print("The encrypted message is:",text_rev1)