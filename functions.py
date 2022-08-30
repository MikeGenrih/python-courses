def sum_of_int(start,end):    # sum of integers
    if end < start:
        start,end = end,start
    else:
        pass
    if start == end:
        return(start)
    else:
        sum = 0
        for i in range(start, end+1):
            sum += i
        return(sum)
print("Sum of integers")
start = int(input("start:  "))
end = int(input("end:  "))
final = print(sum_of_int(start,end))
#######################################################################
#####1000000000 sec  = 31 years 8 mouht 9 days 1 hour 46 min 40 sec

def times(sec):
    import time
    struct = time.gmtime(sec)
    r = (time.strftime("%j:%H:%M:%S",struct))
    r = (":".join(str(int(i)) for i in r.split(":")))   # in this block, I wanted to remove extra zeros
    r = r.split(':')                                    # and the first day from the number of days because it
    r = ([int(i) for i in r])                           # was in the format 001 deys but i wanted 0
    r[0] -=1
    r = ([str(i) for i in r])
    r = (":".join(r))
    return(r)
print("are you intresting how many days are in seconds?")
seconds = int(input("Enter the seconds:  "))
r = print(times(seconds))

# #########################################################################
#
list = [7, 57, 32, 98, 70, 958]
print(f" summa all numbers in the {list=}")
#print(f" Check : {sum(list)}")      # jast Check


def sum(num):
    summa = 0
    for i in num:                     # sum numbers lists with help For
        summa += i
    return summa

sum = print(f' For   : {sum(list)}')
# #################################################
def sums(num):
    count = 0
    summa = 0
    while count < len(num):           # sum nummbers list with help While
        summa += list[int(count)]
        count += 1
        # print(summa)
        # print(count)
    return summa
print(f' While : {sums(list)}')
# #########################################################
#############Recursion
list = [7, 57, 32, 98, 70, 958]
def recursion(sum):
     if sum == []:
         #recursion(sum[len(sum)-1])
         return 0
     else:
         summ = recursion(sum[1:])
         summ += sum[0]
         return summ                     #sum[0]  + recursion(sum[len(sum)+1])

s =(recursion(list))
print(f" Recursion {s}")
#########################################################
#### Fibonachy
def FibonachyREC(n):
    if n == 1 or n == 2:
        return 1

    return FibonachyREC(n - 1) + FibonachyREC(n - 2)
f = int(input("num figure Fibonachi:  "))
print(FibonachyREC(f))
#############################################################
p = "помідор"
m = "м'ясо"
c = "сир"
b = "хліб"

snec = "bun"

def decorator(fu):
    def wrapper():
       print(snec)            # wrapper
       result = fu()
       print(snec)            # wrapper
       return result
    return wrapper


@decorator
def one():
    print(p)
    return None

@decorator
def two():
    print(m)
    return None

@decorator
def three():
    print(c)
    return None

@decorator
def fore():
    print(b)
    return None


o = one()
t = two()
th =three()
f = fore()
