# 1 task here "прав помилку у порівнянні 3 ! 5"
first = 3
second =5

compare = first != second
print(f"task 1 - num_{first=} not equal num_{second=}! it is {compare}")  # here need compare two numbers

# 2 task   Наведи усі комбінації порівняhнь для 5 _ 5, при яких результат буде True
Combination_1 = 5 == 5
Combination_2 = 5 <= 5
Combination_3 = 5 >= 5
Combination_4 = not 5 != 5  # recorrected
Combination_5 = not 5 > 5  ## recorrected
resulr = Combination_1 and Combination_2 and Combination_3 and Combination_4 and Combination_5
print(f"task 2 {Combination_1=}! {Combination_2=}! {Combination_3=} {Combination_4=} {Combination_5=}!") # here result priviouse task
print(f"task 2.1 {resulr=}")

# 3 task here  5 комбінацій з логічних операторів (or, and, not)
# та дужок, так щоб результат у виразі True _ True _ False був True
comb_1 = True or True or False
comb_2 = True and (True or False)
comb_3 = True or True or not False
comb_4 = True and True and not False
comb_5 = (True and True) or False
result = comb_1 and comb_2 and comb_3 and comb_4 and comb_5 # overall result so that everything is True
if (result):
    print(f"task 3 everithing from five comb, is {result}")
if (not result):
    print (f"task 3 error! not everithing from five comb is true")

#  task 4 Порівняй логічні значення None та 7

logik = None and 7
logik2 = None or 7
print(f"task 4 {(bool(logik),bool(logik2))}")

# Порівняй логічні значення пустої строки та виразу 10 - 1

log = (bool("")) and (bool(10-1))   # empty line
log2 = (bool("")) or (bool(10-1))   # empty line
print(f"task 5 {((log),(log2))}")


#print(bool(""))
