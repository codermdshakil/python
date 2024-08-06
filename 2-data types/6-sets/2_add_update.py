
# set1 = set()
# print(set1)

# add elements on set1
# set1.add(8)
# set1.add(5)
# set1.add((5,6))
# print(set1)

# using range based add elements
# for i in range(1, 6):
#     set1.add(i)

# print(set1)

## Using update() Method
# For the addition of two or more elements, Update() method is used. The update() method accepts lists, strings, tuples as well as other Python hash set as its arguments. 


set1 = set([4, 5, (6, 7)])
set1.update([10,11])
print(set1)