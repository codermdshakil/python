## Float

num = 10.5 # float  
# print(type(num))

num1 = 3/4
# print(type(num1)) # float

num2 = 6 * 7.0
# print(type(num2)) # float

## Performing arithmetic operator on float type
a = 1 + 5j
b = 2 + 3j

# Additon
# c = a + b # 11 [without j]
c = a + b # (3 + 8j) [with j]
print("Addition = ", c)

# Subtraction
d = 1 + 5j
e = 2 - 3j

# f = d - e # 7 [without j]
f = d - e  #  (-1 + 8j)  [with j]
print("Substraction = ", f)

# Division
g = 1 + 5j 
h = 2 + 3j 

i = g / h # (1.307692307692308+0.5384615384615384j) [with j]
print("Division:",i)

#Multipication 
j = 1 + 5j
k = 2 + 3j

# Multiplication
l = j * k # (-13+13j) [with j]
print("Multiplication:",l)





