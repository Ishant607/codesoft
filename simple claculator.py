# simple calculator:
a=int(input("enter the value of a:"))
b=int(input("Enter the value of b:"))
o=input("Choose the operator,'+','-','*','/':")
def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
if(o=="+"):
    print(sum(a,b))
elif(o=="-"):
    print(sub(a,b))
elif(o=="*"):
    print(mul(a,b))
elif(o=="/"):
    print(div(a,b))   
else:
    print("invalid input by the user")
    