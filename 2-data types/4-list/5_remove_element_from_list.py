# Removing Elements from the List

### Method 1: Using remove() method
# Remove() method only removes one element at a time, to remove a range of elements, the iterator is used. The remove() method removes the specified item.
# remove() function remove just fast searched value
 
# my_list = [1,2,3,4,5,6,7,8,5,9,10,11,12]
# print("Inisial :", my_list)
# my_list.remove(5)
# print("Results : ", my_list) #[1,2,3,4,6,7,8,'[5]',9,10,11,12] // this 5 not remove
# my_list.remove(8)
# print("Results : ", my_list) #[1,2,3,4,6,7,'[5]',9,10,11,12] // this 5 not remove

# # using iterator method
# for i in range(1, 5): # remove multiple elements using iterator
#     my_list.remove(i)
# print("\nList after Removing a range of elements: ")
# print(my_list)
 

### Method 2: Using pop() method
# pop() function can also be used to remove and return an element from the list, but by default it removes only the last element of the list, to remove an element from a specific position of the List, the index of the element is passed as an argument to the pop() method.

my_list = [1,2,3,4,5,6]
# my_list.pop() # by default remove last elements of the list

#using pop remove a specific value from list sending arguments as index
my_list.pop(2) # index 2 element removed from the list
print(my_list)
