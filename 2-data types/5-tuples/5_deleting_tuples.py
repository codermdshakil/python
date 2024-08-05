### Deleting a Tuple
# Tuples are immutable and hence they do not allow deletion of a part of it. The entire tuple gets deleted by the use of del() method. 

# Note- Printing of Tuple after deletion results in an Error. 

tuples = (1,2,3,4,5,6)
print(tuples)
del tuples ## using del delete entire tuple cause tuple is immuatable for this reason we can't delete a specific element from tuple
