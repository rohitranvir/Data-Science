# Write a program which will accept list of numerical values and find a their squre and squre roots
lst=[float(i) for i in input().split()]
squre=list(map(lambda val:val**2,lst   ))
sqroot=list(map(lambda val:val**0.5,lst))

for i,j in zip(squre,sqroot):
    print(i,"==>>",j)