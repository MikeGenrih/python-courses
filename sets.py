text_1= (input('Enter the text: ')).lower()
text_2 = (input('Enter the other text: ')).lower()

dict_1 = {i for i in text_1 if i.isalpha()}
dict_2 = {i for i in text_2 if i.isalpha()}
output_letter = dict_1 & dict_2
print(f' \nList of letters that are present in both texts is    {". ".join(output_letter)} ')

num_1 = {i for i in text_1 if i.isdigit()}
num_2 = {i for i in text_2 if i.isdigit()}
# print(num_1)
# print(num_2)
# dif_1 = (num_1-num_2)-(num_2-num_1)
# dif_2 = (num_2-num_1)-(num_1-num_2)
print(f' \n Numbers that are in either the first \n set or the second set, but not both'
      f' \n\n first {". ".join(num_1-num_2)} \n\n second {". ".join(num_2-num_1)}\n ')

one = {1, 2, 3, 9}
two ={1, 2, 3, 9, "m", 7, 8}
three = {1, 2, 3, 9, "m", 7, 8, "d", 78,}

print(f" UNION method impoverishes the set and discards the same ones ")

union = one.union(two).union(three)
print(f" union metod:    {union}")
print(f" union operator: {one | two | three}\n")
###################################################

print(f" INTERSECTION show only those elements that are in sets ")
intersection = one.intersection(two).intersection(three)
print(f" intersection metod:    {intersection}")
print(f" intersection operater: {one & two & three}\n")

###########################################################

print(f" DIFFERENCE subtracts the second from the base and shows the remainder ")
Difference = three.difference(two).difference(one)
print(f" intersection metod:    {Difference}")
print(f" intersection operater: {three - two - one}\n")

######################################################


print(f" SYMMETRYC_difference shows elements that are unique in all sets ")
symmetric = three.symmetric_difference(two).symmetric_difference(one)
print(f" symmetric metod:    {symmetric}")
print(f" symmetric operater: {one ^ two ^ three}")