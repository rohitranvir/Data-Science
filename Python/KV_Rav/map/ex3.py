salary=[100,200,300,400]
comm=[10,20,30,40]
totalsal=list(map(lambda sal,com:sal+com, salary,comm ))
for i,j,k in zip(salary,comm,totalsal):
    print(i,"==>",j,"==>",k)