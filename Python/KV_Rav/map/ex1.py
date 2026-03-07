# Write a program which take old salary and increase 20% increment
def increment(sal):
    sal=sal+sal*(20/100)
    return sal
oldsal=[float(sal) for sal in input().split()]
print('List of old sal :',oldsal)
lst=map(increment,oldsal)
z=zip(oldsal,list(lst))
for i,j in z:
    print(i,"==>>",j)