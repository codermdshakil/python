
# Create a list 
# List = ['Shakil', 'Ahmed']

# access list elements using index
# print(List[0]) # Shakil
# print(List[1]) #  Ahmed

# List = [['Shakil', 'Ahmed'], ['Nadim', 'Hassan'], ['Noyon', 'Rahman']]

# # Access elements from multidimentional list 
# print(List[0][0] , List[0][1]) # Shakil Ahmed
# print(List[1][0] , List[1][1]) # Nadim Hassan
# print(List[2][0] , List[2][1]) # Noyon Rahman

## Access elements using Negative Index
List = [1, 2, 'Shakil', 4, 'For', 6, 'Ahmed']
# print(List[-1]) # Ahmed
# print(List[-2]) # 6
# print(List[-3]) # For
# print(List[-5]) # Shakil

## Size of List
# print(len(List)) # 7 

## Input taking from from list
# strings = input("Enter element Separatedly : ")

# # split the strings and store it to list 
# List1 = strings.split()
# print("THe list is  :", List1)
# print the list ['shakil', 'noyon', 'nadim']


## Input size of the list
n = int(input("Enter size of list : "))
# store integers in a list using map,
lst = list(map(int, input("Enter list elements :").split()))[:n] # [:n] using this we can limited list elements
# Print the list 
print(lst)



