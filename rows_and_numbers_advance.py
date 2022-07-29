name = str(input("What is your name"))

str_1 = str.strip(name) #clean the mark

print("letters in the name",len(str_1)) #count letters

result = f"Hello {str.capitalize (str_1)}, nice to e-meet you! "  # {} -> str()

print(result) #show capitalized

print("inverted name",id(str_1))



