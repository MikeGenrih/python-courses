# vocabulary = dict()
# for i in range(0, 257):
#     vocabulary.update({i: chr(i)})
# print(f"{'\n'[::10]vocabulary}")
vocabulary = {i: chr(i) for i in range(0, 257)}

print(str(vocabulary))
#############################################3##
# coder
text = input('Enter text: ')   #  #lipps
key = int(input('enter number from 1 to 25: '))   #4

alp = "abcdefghijklmnopqrstuvwxyz"
import string
alph_dict = dict(zip(string.ascii_lowercase, range(1, 27)))
#print(alph_dict)

new_text = []
for i in text:
    if i in alph_dict:
        new = alph_dict[i] + key
        new = (int(new) - 26) if (int(new) > 26) else new
        new_text.append(list(alph_dict.keys())[list(alph_dict.values()).index(new)])

print(f'your encrypted text: {("".join(new_text))}')


##########################################################
#decoder

text = input('Enter the coder text: ')   #  #lipps
key = int(input('enter same number lake coder just on the contrary from -1 to -25: '))   #4

alp = "abcdefghijklmnopqrstuvwxyz"
import string
alph_dict = dict(zip(string.ascii_lowercase, range(1, 27)))
#print(alph_dict)

new_text = []
for i in text:
    if i in alph_dict:
        new = alph_dict[i] + key
        new = (int(new) - 26) if (int(new) > 26) else new
        new_text.append(list(alph_dict.keys())[list(alph_dict.values()).index(new)])

print(f'your encrypted text: {("".join(new_text))}')