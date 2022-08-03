x = (input("num first"))
#match x1 = "." in (x):
if ("." in (x)):
    x = float(x)
else:
    x = int(x)

print(type(x))
#################################
sign = input("enter the sign")
while not sign in ("+,-,/,*,**,%,"):
    print(f"{sign=} is not correct.+,-,/,*,**,%,")
    sign = input("sign")
#################################
y = (input("num second"))

if ("." in (y)):
    y = float(y)
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
        print("you can't devide by zero")
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
    a = int(a)

else:
    a = float(a)
print(type(a), a)




