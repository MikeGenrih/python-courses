x = (input("num first"))
#match x1 = "." in (x):
if ("." in (x)):
    x = float(x)                                     # in this block the text from the user
else:                                                # is converted to an integer or fractional number
    x = int(x)

print(type(x))
#################################
sign = input("enter the sign")
while not sign in ("+,-,/,*,**,%,"):                 #in this block, I tried to loop the code
    print(f"{sign=} is not correct.+,-,/,*,**,%,")   # until the user enters the correct sign
    sign = input("sign")
#################################
y = (input("num second"))

if ("." in (y)):                                     #in this block the text from the user
    y = float(y)                                     # is converted to an integer or fractional number
else:
    y = int(y)

print(type(y))
##################################

if sign == "+":
    a = (x + y)
elif sign == "-":
    a = (x - y)
elif sign == "/":
    if y == 0:
        print("you can't devide by zero")            # here are the calculations of the calculator
    else:
       a = (x / y)

elif sign == "*":
    a = (x * y)
elif sign == "**":
    a = (x ** y)
elif sign == "%":
    a = (x % y)
else:
    print("something wrong try again ")

###################################  4.0000
b = int(a)
if b == a:
    a = int(a)                                         #The calculator must return a result of type int if the operands
                                                       # wereof type int. Or return a float if at least one operand was
else:                                                  # a float
    a = float(a)
print (f" {x}{sign}{y} = {a} answer is {(type(a))}")
###################################




