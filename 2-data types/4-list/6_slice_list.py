## Slicing of a List
# print a specific range of elements from the list, we use the Slice operation. 

## slice a specific range: [ start index : end index]
## To print elements from beginning to a range, use: [: Index]
## To print elements from begining to negative range, use: [:-Index]
## To print elements from a specific Index till the end, use : [Index:]
## To print elements from a specific negative Index till the end, use  : [-Index:]
## To print the whole list in reverse order, use  : [::-1]

# Creating a List
List = ['G', 'E', 'E', 'K', 'S', 'F',
        'O', 'R', 'G', 'E', 'E', 'K', 'S']
print("Initial List: ")
print(List)

# # using Slice operation
# # range based slice
# Sliced_List = List[3:8]
# # print(Sliced_List)

# # pre-defined point to end
# # a specific index to end
# Sliced_List = List[5:] # 5 to end
# print("\nElements sliced from 5th element till the end: ")
# # print(Sliced_List)


# # beginning till end
# Sliced_List = List[:]
# # print(Sliced_List)


### Negative index List slicing

# to a pre-defined point using Slice 
Sliced_List = List[:-6]
print(Sliced_List)

# using negative index List slicing
Sliced_List = List[-6:-1]
print("\nElements sliced from index -6 to -1")
print(Sliced_List)

# Printing elements in reverse
# using Slice operation
Sliced_List = List[::-1]
print("\nPrinting List in reverse: ")
print(Sliced_List)

