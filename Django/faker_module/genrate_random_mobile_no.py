from random import *
def phonenumbergen():
    d1=randint(6,9)
    num=""+str(d1)
    for i in range(9):
        num+=str(randint(0,9))
    return int(num)
for i in range(10):
    print(phonenumbergen())