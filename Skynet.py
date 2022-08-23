t = 00001

r = [001,4,7]
r = int(r.split(':'))

r[1] -=1
r = ":".join(r)
print(r)