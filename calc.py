import math
import random
def add(a,b):
    a=float(a)
    b=float(b)
    print(a+b)
def multiply(a,b):
    print(float(a)*float(b))
def divide(a,b):
    a=float(a)
    b=float(b)
    if b==0:
        print("divide by zero error")
    else:
        print(a/b)
def subtract(a,b):
    a=float(a)
    b=float(b)
    print(a-b)
def square_root(a):
    a=float(a)
    if a<0:
        b=a*-1
        print(str(math.sqrt(b)) + "i")
    if a!=0 and a>0:
        print(math.sqrt(a))
def power(a,b):
    a=float(a)
    b=float(b)
    if a==0 and b==0:
        print("0 to the power of 0 is undefined")
    else:
        print(a**b)
def cos(a):
    a=float(a)
    print(math.cos(a))
def sin(a):
    a=float(a)
    print(math.sin(a))
def tan(a):
    a=float(a)
    print(math.tan(a))
def cot(a):
    a=float(a)
    print(1/math.tan(a))
def log(a):
    a=float(a)
    print(math.log(a))
def random_number(a):
    a=float(a)
    b=random.randint(1,50)
    c=a*b
    d=c/2
    e=5+d
    f=e/random.randint(1,5)
    g=2+e
    h=g/2
    print(h)
def factorial(a):
    a=int(a)
    if a==0 or a==1:
        print(1)
    else:
        print(math.factorial(a))
def inverse(a):
    a=float(a)
    print(1/a)
def absolute_value(a):
    a=float(a)
    if a<0:
        print(a*-1)
    else:
        print(a)
option="16"
while True:
    print("1. add")
    print("2. multiply")
    print("3. divide")
    print("4. subtract")
    print("5. square root")
    print("6. power")
    print("7. cos")
    print("8. sin")
    print("9. tan")
    print("10. cot")
    print("11. log")
    print("12. random number generator")
    print("13. factorial")
    print("14. absolute value")
    print("15. inverse")
    print("16.exit")
    option=input()
    if option=="1":
        a=input("enter number one: ")
        b=input("enter number two: ")
        c=float(a)
        d=float(b)
        add(c,d)
    elif option=="2":
        a=input("enter number one: ")
        b=input("enter number two: ")
        multiply(a,b)
    elif option=="3":
        a=input("enter number one: ")
        b=input("enter number two: ")
        divide(a,b)
    elif option=="4":
        a=input("enter number one: ")
        b=input("enter number two: ")
        subtract(a,b)
    elif option=="5":
        a=input("enter number one: ")
        square_root(a)
    elif option=="6":
        a=input("enter number one: ")
        b=input("enter number two: ")
        power(a,b)
    elif option=="7":
        a=input("enter number one: ")
        cos(a)
    elif option=="8":
        a=input("enter number one: ")
        sin(a)
    elif option=="9":
        a=input("enter number one: ")
        tan(a)
    elif option=="10":
        a=input("enter number one: ")
        cot(a)
    elif option=="11":
        a=input("enter number one: ")
        log(a)
    elif option=="12":
        a=input("enter number one: ")
        random_number(a)
    elif option=="13":
        a=input("enter the first number: ")
        factorial(a)
    elif option=="14":
        a=input("enter number one: ")
        absolute_value(a)
    elif option=="15":
        a=input("enter number one: ")
        inverse(a)
    elif  option=="16":
        exit()
    else:
        print("invalid operation")
    


    
