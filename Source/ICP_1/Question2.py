# import random library for random int
import random as r

# create input STR string
string = str(input("Enter PYTHON as a string "))

# get two random ints from 0 to length and remove that corresponding index from the string
int1 = r.randint(0,len(string)-1)
newstr = string.replace(string[int1],'',1)

int2 = r.randint(0,len(newstr)-1)
newstr2 = newstr.replace(newstr[int2],'',1)

# reverse the final string
reversestr = newstr2[::-1]

# print answer
print(reversestr)

# placeholder line for console print
print("______________________________\n")

# input 2 numbers
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

# perform and print arithmetic results
print("Add = ", num1, " + ", num2, " = ", num1+num2)
print("Minus = ", num1, " - ", num2, " = ", num1-num2)
print("Multiply = ", num1, " * ", num2, " = ", num1*num2)
print("Divide = ", num1, " / ", num2, " = ", num1/num2)