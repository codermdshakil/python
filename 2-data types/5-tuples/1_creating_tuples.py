# Tuples
# Immutable, meaning once a tuple is created, you cannot modify, add, or remove elements.

### Creating empty tuples
Tuples = ()
# print("Print empty Tuples ", Tuples)

## Create a tuples with string value
Tuples = ('Shakil Ahmed', 'Noyon Rahman')
# print(Tuples)

## Create tuples with number value
Tuples = (1,2,3,4,5,6)
# print(Tuples)

# Creating tupls using build in function 
Tuple1 = tuple('shakil') # ('s', 'h', 'a', 'k', 'i','l')
# print(Tuple1)


## Creating tuple using mixed data types
Tuple1 = (5, 'wecome', 'shakil', 'ahmed', False)
# print(Tuple1)

## Createte a tuple with nested tuple

Tuple1 = (0,1,2,3)
Tuple2 = ('python', 'master')
Tuple3 =  (Tuple1, Tuple2)
# print(Tuple3)

# Creating a Tuple
# with the use of loop
Tuple1 = ('Python')
n = 5
print("\nTuple with a loop")
for i in range(int(n)):
    Tuple1 = (Tuple1,)
    print(Tuple1)

