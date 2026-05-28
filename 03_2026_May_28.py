'''Date : 28th MAY 2026 
Topic : Control flow and Conditional statements, Modulo operator'''

# Syntax 
'''
If condition:
    # code to execute if condition is true
elif another_condition:
    # code to execute if another_condition is true
else:
    # code to execute if all conditions are false
'''

#roller coster 
print("Welcome to the roller coster!")
height = int(input("Enter your height in cm: "))
if height >=120:
    print("You can ride the roller coster!")
else:
    print("Sorry, you need to be at least 120cm tall to ride the roller coster.")

# Modulo operator
# The modulo operator (%) returns the remainder of a division operation.
# For example:
print(10 % 3) #output 1
print(15 % 4) #output 3

#Odd Even number using Modulo : 
number = int(input("Enter a number: "))
if number % 2 == 0 :
    print("The number is even")
else : 
    print("The number is odd")

#Nested If else statement:
print("Start")
height = int(input("Enter you height in cm: "))
age = int(input("Enter your age:"))
if height>=120:
    if age >= 18:
        print("You can ride the roller coster!")
    elif age >= 12:
        print("You can ride the roller coster with an adult!")
    else:
        print("Sorry, you need to be at least 18 years old to ride the roller coster.")
else:
    print("Sorry, you need to be at least 120cm tall to ride the roller coster.")
    
#Logical Operators: 

# and >> Both the conditions are true
# or >> At least one condition is true
# not >> negates the condition
# Example:
age = int(input("Enter your age: "))
if age >= 18 and age < 60:
    print("You are an adult.")
elif age >= 60:
    print("You are a senior citizen.")
else:
    print("You are a minor.")       

##Treasure Island: 
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right' ").lower()
if choice1 == "left":
    choice2 = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")   

