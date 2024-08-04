# Removing Elements from the List

### Method 1: Using remove() method
# Remove() method only removes one element at a time, to remove a range of elements, the iterator is used. The remove() method removes the specified item.
# remove() function remove just fast searched value
 
my_list = [1,2,3,4,5,6,7,8,5,9,10,11,12]
print("Inisial :", my_list)
my_list.remove(5)
print("Results : ", my_list) #[1,2,3,4,6,7,8,'[5]',9,10,11,12] // this 5 not remove
my_list.remove(8)
print("Results : ", my_list) #[1,2,3,4,6,7,'[5]',9,10,11,12] // this 5 not remove

# using iterator method
for i in range(1, 5): # remove multiple elements using iterator
    my_list.remove(i)
print("\nList after Removing a range of elements: ")
print(my_list)
 
