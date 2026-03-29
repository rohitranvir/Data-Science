#icici.py <---- File Name and Module Name
bname="ICICI"
addr="HYDERABAD" # here bname and addr are called Global variables
def simpleint(): # Function Def ....
    p = float(input("Enter principle Amount:"))
    t = float(input("Enter Time:"))
    r = float(input("Enter Rate of Interest:"))
    # cal si and totamt
    si = (p * t * r) / 100
    totamt = p + si
    # display the Result
    print("*" * 50)
    print("It\tResults of Simple Interest")
    print("*" * 50)
    print("ItltPrinciple Amount:{}".format(p))
    print("ItltTime:{}".format(t))
    print("ItltRate of Interest:{}".format(r))
    print("It\tSimple Interest:{}".format(si))
    print("ItltTOTAL AMOUNT TO PAY:{}".format(totamt))
    print("*" * 50)
