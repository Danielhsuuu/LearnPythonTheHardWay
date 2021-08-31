from sys import argv
#takes two arguments
script, filename = argv 
#open a file whose name is the same as the text held by txt
txt = open(filename)

#prints Here's your file '(filename)':
print("Here's your file %r:" % filename)
#prints the content of the file
print(txt.read())
#prints Type the filename again:
print("Type the filename again:")
#prints > and takes the user's input and store it into a variable named file_again
file_again = input("> ")

#open a file whose name is the same as the text held by txt_again
txt_again = open(file_again)
#prints the content of the file
print(txt_again.read())