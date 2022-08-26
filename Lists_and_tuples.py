# 1 . string from the user and prints every third word
user = input('Enter any sring: ')
                                                       #seafood crab massels prawns salmon squid tuna beef chicken duck
print(f'every third word:{}')

# 2  list comprehension
initial_list = [1,2.1,"f","2",3,"1",18,"df",]

print(f"{initial_list=}")
                                       #[1,2.1,-1,"6",9,"3",18,-1]
output_list = [el if type(el) == float
               else el if type(el) == int and el%2 == 0 else el**2 if type(el) == int and el%2 != 0
               else (str(int(float(el)*3)))  if type(el) == str and  el.isdigit() else -1 for el in initial_list]

print(f"{output_list=}")

print("    example=[1, 2.1, -1, '6', 9, '3', 18, -1]")