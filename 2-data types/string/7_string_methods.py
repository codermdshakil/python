
# Note: Every string method in Python does not change the original string instead returns a new string with the changed attributes. 

text = "Shaki AhMed"

# upper() function to convert string to upper case
print(text.upper())

#lower() function to convert string to lower case
print(text.lower())

#title() converts the first character to upper case and rest to lower case 
print(text.title())

#swapcase() convert upper to lower and lower to upper
print(text.swapcase())

#capitalize() convert first character Upper in string
print(text.capitalize())

#Remove whitespaces 
my_string = "   Hello, world!   "
stripped_string = my_string.strip() 
print(stripped_string)
