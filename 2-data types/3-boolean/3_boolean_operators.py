
## Boolean Operators
# or 
# and 
# not
# == (equivalent)
# != (not equivalent)

### Boolean OR Operator : if one value true then true
# a = 1
# b = 2
# c = 4

# if a> b or b < c:
#     print("True")
# else:
#     print("False")

# if a or b or c:
#     print("True")

### Boolean AND Operator : Both value must be True then True otherwise  if one value is False then result false
# a = 0
# b = 2
# c = 4

# if a> b and b < c:
#     print(True)
# else:
#     print(False)

# if a and b and c:
#     print("All the number boolean value as True")
# else:
#     print("Atleast one number has boolean value as False")

### Boolean NOT Operator : !true = false,  !false = true
# a = 0
  
# if not a: 
#     print("Boolean value of a is False")
# else:
#     print("Boolean value is true")

### Boolean Equal Operator 
# a = 5
# b = 10

# if a == b:
#     print("Yes a and b are Equal")
# else:
#     print("No they are not Same!")


### Boolean Is Operator
# The is keyword is used to test whether two variables belong to the same object. The test will return True if the two objects are the same else it will return False even if the two objects are 100% equal.

a = 10
b = 10
if a is b:
    print("Yes")
else:
    print("No")

# The code first assigns the value 10 to variables x and y. It then compares x and y using the “is” operator and prints True because they refer to the same object. Next, it assigns two separate lists to x and y. It then compares x and y using the “is” operator and prints False because the lists are different objects in memory. 

x = ["a", "b", "c", "d"] 
y = ["a", "b", "c", "d"] 

print(x is y)