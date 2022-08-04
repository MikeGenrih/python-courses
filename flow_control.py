x = (input("num first--->"))
#match x1 = "." in (x):
x = float(x) if ("." in (x)) else int(x)         # in this block the text from the user
                                                     # is converted to an integer or fractional number
print(f"type num first is {type(x)}")                 #recorrect
#################################
sign = input("enter the sign--->")
while not sign in ("+-/**%"):                        #in this block, I tried to loop the code
    print(f"{sign=} is not correct.+,-,/,*,**,%,")   # until the user enters the correct sign
    sign = input("sign")
#################################
y = (input("num second--->"))

y = float(y) if ("." in (y)) else int(y)

print(f"type num second is {type(y)}")              #recorrect
##################################

if sign == "+":
    a = x + y
elif sign == "-":
    a = x - y
elif sign == "/":
    if y == 0:
        print("you can't devide by zero")            # here are the calculations of the calculator
    else:
       a = x / y

elif sign == "*":
    a = x * y
elif sign == "**":
    a = x ** y
elif sign == "%":
    a = x % y
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

if x > y:
    print(f"{x} more {y}")
elif x ==y:
    print(f"{x} same {y}")                             # comparing two numbers
else:
    print(f"{x} less {y}")
####################################
print( f" digit number {len(str(a))}")