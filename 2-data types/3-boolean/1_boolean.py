# Boolean represents just two value True or False 
a = 1 == 1
# print(a) # True

b = 2 < 1
# print(b) # False

## We can evaluate values and variables using the Python bool() function. This method is used to return or convert a value to a Boolean value i.e., True or False

x = 5
y = 10
# print(bool(x == y)) #False  Returns False as x is not equal to y 

x = None 
# print(bool(x)) # false
x = ()
# print(bool(x)) # false

x = {}
# print(bool(x)) # False

x = 0.0
# print(bool(x)) # False

x = "Shakil Ahmed"
print(bool(x))


