## Set items cannot be accessed by referring to an index, since sets are unordered the items has no index. But you can loop through the Python hash set items using a for loop, or ask if a specified value is present in a set

# Creating a set
set1 = set(["Geeks", "For", "Geeks."])
# print(set1)

# print all elements from sets

# for i in set1:
#     print(i, end=" ")


## Remove elements from sets
set1 = [1,2,3,4,5,6,7,8,9,10,11,12]
print(set1)

# Removing elements from Set  using Remove() method
set1.remove(5)
set1.remove(6)
print(set1)


# Removing elements from Set using iterator method
for i in range(1, 5):
    set1.remove(i)
print("\nSet after Removing a range of elements: ")
print(set1)