import functools
def sumop(x,y):
    return x+y
lst=[10,20,30,40,50]
res=functools.reduce(sumop ,lst)
print(res)