# wpp which will find max values from list of numbers by using reduce function
import functools
lst=[10,50,30,40,50]
res=functools.reduce(lambda  k,v : k if k>v else v,lst)
print("max({}) = {}".format(lst,res))
