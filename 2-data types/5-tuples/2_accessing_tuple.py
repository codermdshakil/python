## Accessing of Tuples
# In Python Programming, Tuples are immutable, and usually, they contain a sequence of heterogeneous elements that are accessed via unpacking or indexing (or even by attribute in the case of named tuples). Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.

# Note: In unpacking of tuple number of variables on the left-hand side should be equal to a number of values in given tuple a


### Accesing tuples using index
tuple1 = tuple('python')
# print first element of tuple
# print(tuple1[3])

# tuple unpaking
tuple1 = ('python', 'is', 'easy')
a, b, c = tuple1
print(a) #python
print(b) # is
print(c) # easy



