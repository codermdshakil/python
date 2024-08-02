
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
a = 0
b = 2
c = 4

if a> b and b < c:
    print(True)
else:
    print(False)

if a and b and c:
    print("All the number boolean value as True")
else:
    print("Atleast one number has boolean value as False")
