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
# print("sum of integers")
# start = int(input("start:  "))
# end = int(input("end:  "))
# final = print(sum_of_int(start,end))
# #######################################################################
# 1000000000 sec  = 31 years 8 mouht 9 days 1 hour 46 min 40 sec

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
# print("are you intresting how many days are in seconds?")
# seconds = int(input("Enter the seconds:  "))
# r = print(times(seconds))

#########################################################################
list = [7, 57, 32, 98, 70, 958]

def sum(num):
    counter = 0
    for i in num:                     # sum numbers lists
        counter += i
    return counter

sum = print(f' For : {sum(list)}')

def sum(num):
	count = 0
	while count < len(num):
		sum = sum(num)
		count += 1
	return sum
print(f' While : {sum(list)}')