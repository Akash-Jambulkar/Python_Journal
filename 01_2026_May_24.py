'''Date : 24 MAY 2026
   Day : Sunday
   Topic : print command, Input function'''

#indentation is not required in python but it is a good practice to use it to make the code more readable. It is also used to define a block of code.

##Print Command :
print("Hello World") 
#The first line shows the location of the file and the second line is the output of the print command.
#Anything inside double quotes will be printed as it is. We can also use single quotes to print the same thing it is called String.
#Standard practice is to add a new line after the print command to make the code more readable.

print("First line\nSecond line") #using \n we can print new line in the same print command. It is called escape sequence.

print("First line\tSecond line") #using \t we can print a tab space in the same print command. It is also an escape sequence.

print("Concanenation of" + " " + "two strings") #Concatenation means joining two strings together. We can use + operator to concatenate two strings.

##Input Funtion and Variable: 
name = input("Enter your name: ") #input function is used to take input from the user. It takes a string as an argument which is displayed as a prompt to the user.
print("Hello " + name) #we can use the input function to take input from the user and then use it in the print command to display a message. In this case, we are taking the name of the user and then greeting them with their name.

##Len function : 
length = len(name) #len function is used to find the length of a string. 

##Variable Naming :
#Variable names should be meaningful and should not start with a number. They can contain letters, numbers and underscores but cannot contain spaces. It is a good practice to use lowercase letters for variable names and separate words with underscores.
#For example, if we want to store the age of a person, we can use the variable name "age" instead of "a" or "age_of_person". It is also a good practice to use descriptive variable names that indicate the purpose of the variable. For example, if we want to store the name of a person, we can use the variable name "name" instead of "n" or "name_of_person". This makes the code more readable and easier to understand.

##Created a Band Name Generator
print("Welcome to the Band Name Generator")
city = input("What city did you grow up in? ")
pet = input("What is the name of your pet? ")
band_name = city + " " + pet
print("Your band name could be " + band_name) #we are taking the city and pet name from the user and then concatenating them to create a band name. We are also adding a space between the city and pet name to make it more readable. Finally, we are printing the band name to the user.          
