symba = input("enter any symbols: ")
#print(str.upper(symba))
#print(f"Up letters: {symba.upper()}")

vowels, spase, figures, up = ([],[],[],[])

comparison_with = ['a', 'e', 'i', 'o', 'u', 'y']

for i, letter in enumerate(symba):

    if letter in "aeiouyAEIOUY":
        vowels.append(letter)

    if letter == " ":
        spase.append(i)

    if letter.isupper():                                   # up registr
        up.append(letter)

    try:
        if letter.isdigit():
            if symba[i + 1].isdigit() and symba[i + 2].isdigit():
                figures.append(symba[i])
                figures.append(symba[i + 1])
                figures.append(symba[i + 2])
                print("3 figures is finded.")
                break
            else:
                None
    except IndexError as error:
        None
        continue
print(f"{''.join(vowels)}")
print(f"{''.join(up)}")
print(f"space: {' '.join(str(i) for i in spase)}")




# symba = input("enter any symbols:")
# symba2 = list(symba)
# symba = str.upper(symba)
# print(symba)
# ######################
#
# ######################                  #print(symba2) join(symba2)
# for index, letter in enumerate(symba):
#     if letter == " ":                                 # # spase
#         print(f'space  {index=} ')
# ######################
#
# d = []
# for el in symba2:
#     if el.isupper():                                   # up registr
#         d.append(el)
#     else:
#         pass
# d = "".join(d)
# print(d)
#
# ###################################
# #vowels = ['a', 'e', 'i', 'o', 'u', 'y']
#
# symba3 = (list(filter(lambda x: x[0].lower() in "aeiouy", symba2)))   # <----
#
#
#
# symba3 = "".join(symba3)
# print(symba3)
# #######################
#
# num = """"""
# for i in symba:
#     if i.isdigit():                                       # 3 figures
#         num = num + i
#     if len(num) >= 3:
#         print("3th figures includ's in synbols")
#         break
# else:
#     print("work is done correct")
#
# #############################
# #for i in range(3):
#    # print(symba)
# ##########################

