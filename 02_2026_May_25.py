'''Date : 25 MAY 2026
   Day : Monday
   Topic : Data types, Type Casting, Mathematical Operations'''

#Data types

#String
print("This is a String")

#Numbers
print(1234) #Integer
print(3.14) #Float

#Boolean
print(True)

#Subscripting
print("Hello"[0]) #H
print("Hello"[1]) #e
print("Hello"[2]) #l
print("Hello"[3]) #l
print("Hello"[4]) #o

#TypeCasting : Converting one data type to another
print(int(3.14)) #3
print(float(1234)) #1234.0
print(str(1234)) #"1234"

#Mathematical Operations :
print(2 + 3) #Addition 5
print(5 - 2) #Subtraction 3
print(4 * 3) #Multiplication 12
print(10 / 2) #Division 5.0
print(10 // 3) #Floor Division 3
print(10 % 3) #Modulus 1
print(2 ** 3) #Exponentiation 8

#parentheses will always be evaluated first
print(2 + 3 * 4) #14
print((2 + 3) * 4) #20

#Number Manipulation and F Strings
#number manipulation is the process of performing mathematical operations on numbers to get a desired result. It is also used to format numbers in a specific way. For example, we can use f strings to format numbers to a specific number of decimal places or to add a currency symbol.
score = 0
score += 1 #score = score + 1
print(f"Your score is {score}") #f string is used to format the string and it is denoted by the letter f before the string. We can use curly braces {} to insert the value of a variable inside the string. In this case, we are inserting the value of the variable score inside the string. This is a more readable and efficient way to format strings compared to concatenation.

#round function 
print(round(3.14159, 2)) #3.14

#assignment operators
x = 5
x += 2 #x = x + 2
print(x) #7
x -= 2 #x = x - 2
print(x) #5
x *= 2 #x = x * 2
print(x) #10
x /= 2 #x = x / 2
print(x) #5.0
x //= 2 #x = x // 2
print(x) #2.0
x %= 2 #x = x % 2
print(x) #0.0


#Tip Calculator
bill = float(input("Enter the total bill amount: "))
tip_percentage = float(input("Enter the tip percentage you want to give: "))
tip_amount = bill * (tip_percentage / 100)
total_amount = bill + tip_amount
split = int(input("Enter the number of people to split the bill: "))
print(f"Your tip amount is: {tip_amount:.2f}")
print(f"Your total amount is: {total_amount:.2f}")
print(f"Each person should pay: {total_amount / split:.2f}")


