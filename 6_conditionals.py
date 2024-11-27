 
 
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


marks = 75

if marks >= 95 and marks <= 100:
    print("You get golden A+")
elif marks >= 80 and marks < 95:
    print("You get A+")
elif marks >= 70 and marks < 80:
    print("You get A")
elif marks >= 60 and marks < 70:
    print("You get A")
elif marks >= 50 and marks < 60:
    print("You get A-")
elif marks >= 40 and marks < 50:
    print("You get B")
elif marks >= 33 and marks < 40:
    print("You get C") 
elif marks < 33:
    print("You are Fail")
else:
    print("Enter your number again")
   
