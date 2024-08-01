
## using formet() string can formetted :
#  Format method in String contains curly braces {} as placeholders which can hold arguments according to position or keyword to specify the order.

## Print in default order
string1 = "{} {} {} {}".format('My', 'Name', 'Shakil', 'Ahmed') #here you can use single or double quatation
# print default order 
# print(string1)

## positional fomatting
string2 = "{1} {0} {3} {2}".format("Name", "My", "Ahmed", "Shakil")
# My name Shakil Ahmed
# 0   1   2      3      
# print(string2)

## Keyword formetting
string3 = "{m} {n} {i} {s} {a} ".format(m="My", i="is" , s="Shakil", n="Name", a="Ahmed")
print(string3)


