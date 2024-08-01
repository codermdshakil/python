# 1. Update a character
#------------------------
# strings = "Hello, I'm Shakil"
# print(strings)

# Updating a character of the String
## As python strings are immutable, they don't support item updation directly
### there are following two ways

#1 using list then operation then string

# covert string to list/array
# list1 = list(strings)
# # access second element and change value 
# list1[1] = 'p'
# # convert list/array to string 
# string2 = "".join(list1)
# # print updated character string 
# print(string2) # Hpllo, I'm Shakil

#2 using slice method

# string3 = strings[0:2] + 'p' + strings[3:] 
# print(string3) # Heplo, I'm Shakil 

# 2. Update entire string
#----------------------------

# In Python Programming, As Python strings are immutable in nature, we cannot update the existing string. We can only assign a completely new value to the variable with the same name.
# string1 = "I want to be a teacher"
# string1 = "I want to be a programmer"
# print(string1)

## Delete a character
# ----------------------

# string1 = "Shakil Ahmed"
# print(string1) # Shakil Ahmed
# # delete a character in index [2]
# list1 = list(string1)
# del list1[2]
# deleted_string = "".join(list1)
# print(deleted_string) #Shkil Ahmed - delete 2 index value

## Delete entire string
# string1 = "Shakil"
# print(string1)
# del string1 
# this is not good to delete string value but forcefully can posible 
# list1 = list(string1)
# list1[0] = ' '
# list1[1]= ' '
# list1[2] = ' '
# list1[3] = ' '
# list1[4] = ' '
# list1[5] =  ' '
# string2 = "".join(list1)
# print(string2)