## Sets

# Creating sets
my_set = {1,3,4,2,5}
print(my_set)


# Creating sets with string
set1 = set("Shakil")
# print(set1)
strings = "shakilahmed"
set1 = set(strings)


#Create sets with list
set1 = set(['shakil', 'noyon', 'nadim'])
# print(set1)


# Creating sets using tuples
t = tuple( 'shakil')
set1 = set(t)
# print(set1)

# creating a sets using dictonary
d = {'geeks':0,'for':1,'geeks':2 }
set1 = set(d)
# print(set1)

# Creating a Set with a List of Numbers
# (Having duplicate values)
set1 = set([1, 2, 4, 4, 3, 3, 3, 6, 5 , 8 , 7 ,10]) # {1, 2, 3, 4, 5, 6}
# print(set1)

# Creating a Set with a mixed type of values
# (Having numbers and strings)
set1 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks']) # {1, 2, 4, 6, 'Geeks', 'For'}
# print(set1)