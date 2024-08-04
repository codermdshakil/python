# Inisial List is black
List = []
# print(List)
### Method 1 : append() -> append() method only works for the addition of elements at the end of the List

# List.append(10)
# List.append(20)
# List.append(30)
# List.append(40)
# List.append(50)
# print(List)

### Added elements to the list using Iterator
for i in range(1, 5):
    List.append(i)
print("Print list after adding elements 1 - 4 : ")
print(List)


### Adding Tuples to the list
List.append((5, 10))
print(List)

### Adding list in list
List1 = ['Shakil', 'Ahmed']
List.append(List1)
print(List)



