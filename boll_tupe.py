# 1 task here "прав помилку у порівнянні 3 ! 5"
first = 3
second =5

compare = first != second
print(f"num_{first=} not equal num_{second=}! it is {compare}")  # here need compare two numbers

# 2 task here   Наведи усі комбінації порівнянь для 5 _ 5, при яких результат буде True
Combination_1 = 5 == 5
Combination_2 = 5 <= 5
Combination_3 = 5 >= 5
resulr = Combination_1 and Combination_2 and Combination_3
print(f"{Combination_1=}! {Combination_2=}! {Combination_3=}!") # here result priviouse task
print(f"{resulr=}")

# 3 task here  5 комбінацій з логічних операторів (or, and, not)
# та дужок, так щоб результат у виразі True _ True _ False був True
comb_1 = True or True or False
comb_2 = True and (True or False)
comb_3 = True or True or not False
comb_4 = True and True and not False
comb_5 = (True and True) or False
result = comb_1 and comb_2 and comb_3 and comb_4 and comb_5 # overall result so that everything is True
if (result):
    print(f"everithing from five comb, is {result}")

#  task 4 Порівняй логічні значення None та 7






