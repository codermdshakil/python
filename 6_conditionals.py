 
 
# marks = int(input("Enter your marks: "))
# print(marks)

# age = 17
# # condition start from here
# if age >= 18:
#     print("You can Vote")
#     print("You can get driving lysence")
# else:
#     print("You can't Vote")
#     print("You can't get driving lysence")


## Example 1 : if, elif, else

# marks = 75

# if marks >= 95 and marks <= 100:
#     print("You get golden A+")
# elif marks >= 80 and marks < 95:
#     print("You get A+")
# elif marks >= 70 and marks < 80:
#     print("You get A")
# elif marks >= 60 and marks < 70:
#     print("You get A")
# elif marks >= 50 and marks < 60:
#     print("You get A-")
# elif marks >= 40 and marks < 50:
#     print("You get B")
# elif marks >= 33 and marks < 40:
#     print("You get C") 
# elif marks < 33:
#     print("You are Fail")
# else:
#     print("Enter your number again")
   

## Example 2 : if, elif, else
# Trafic lights code

# light = input("light : ")

# if (light == "red"):
#     print("Stop")
# elif (light == "green"):
#     print("Go")
# elif (light == "yellow"):
#     print("Look")
# else:
#     print("Light is Broken")
    
    
    
## Single line Condition or Ternary Operator

food = input("food : ")
eat = "YES" if food == "cake" else "NO"
print(eat)



    
"""
AND, OR rules

  AND (if one value is false result is false)
------
TT -> T
FT -> F
TF -> F
FF -> F
 
  OR (if one value is true then result is true)
-----
TT -> T
FT -> T
TF -> T
FF -> F


"""