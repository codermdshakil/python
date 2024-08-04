# Inisial List is black
# List = []
# print(List)
### Method 1 : append() -> append() method only works for the addition of elements at the end of the List

# List.append(10)
# List.append(20)
# List.append(30)
# List.append(40)
# List.append(50)
# print(List)

### Added elements to the list using Iterator
# for i in range(1, 5):
#     List.append(i)
# print("Print list after adding elements 1 - 4 : ")
# print(List)


### Adding Tuples to the list
# List.append((5, 10))
# print(List)

### Adding list in list
# List1 = ['Shakil', 'Ahmed']
# List.append(List1)
# print(List)

### Method 2 : Insert() -> Insert take two arguments (position, value). using insert function we can insert a value in a specific index of list
# List = [1,2,3,4]
# print("Inisial List :", List)
# adding a elements a specific position
# List.insert(0, 10)
# List.insert(3, "Shakil")
# print(List)

### Method 3: Using extend() method :  extend(), this method is used to add multiple elements at the same time at the end of the list 
# Note: append() and extend() methods can only add elements at the end.

List = [1,2,3,4,5]
List.extend([6,7,8,9])
List.extend(['Sagor', 'Shakil', 'Saykot', 'Siam'])
print(List)
