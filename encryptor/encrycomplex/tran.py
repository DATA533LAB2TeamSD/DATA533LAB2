import random
def tran(a):
    e = ''
    i = random.sample(range(len(a)),len(a))
    for index in i:
        e += a[index]
    return e
