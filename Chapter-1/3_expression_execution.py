
## Expression Execution

# Rule 1:  Strinig & Numeric values can operate together with * 

# A, B = 2, 3
# txt = "@"
# print(A*txt*B) ## output = @@@@@@

# Rule 2: string & string can operate with + or Concatination
# A, B = "2", 3
# txt = "@"
# print((A + txt) * B) ## oupput = 2@2@2@

#Rule 3 : Numetic vales can operate with all arithmetic operators

# A, B = 2,3
# C = 4
# print(A + B * C) # 14 -- * > + first priority is Multipication


# Rule 4 : Arithmetic exprssion with integer and float will result in float

# A, B = 10, 5.0
# C = A * B
# print(C) # 50.0

## Floor gives closest integer, which is leasser than or  Equal to the flaot value

# Results of (A//B) is the same as floor(A/B)

# A, B = 12, 5
# C = A//B
# print(C) # 2

# Remainder is Negative when denominator is negative
# A, B = -5, 2
# C = A%B
# print(C) # 1

A, B = 5, -2
C = A%B
print(C) # -1













