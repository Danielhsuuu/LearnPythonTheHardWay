#an error occurs when less than 4 arguments are given because the the code needs four in order to work

from sys import argv
script, first, second, third = argv
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

fourth = input("enter fourth ")

print(fourth)