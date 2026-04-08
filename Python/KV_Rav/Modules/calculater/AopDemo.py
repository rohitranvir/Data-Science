from menu import menu
from operation import *
import sys
menu()

while(True):
    ch = int(input("Enter your Choice : "))
    match(ch):
        case 1:
            print(add())
        case 2:
            print(sub())
        case 3:
            print(mul())
        case 4:
            print(div())
        case 5:
            print(moddiv())
        case 6:
            print(expo())
        case 7:
            print("Thank For using My program")
            sys.exit()
        case _:
            print("Your selection of program is wrong ")
