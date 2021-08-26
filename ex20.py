from sys import argv

script, input_file = argv

#defines a function named print_all that takes an argument named f
def print_all(f):
    #prints the contents of file f
    print(f.read())

#defines a function named rewind that takes an argument named f
def rewind(f):
    #goes back to the zeroth byte in file f
    f.seek(0)

#defines a function named print_a_line that takes two arguments named line_count and f
def print_a_line(line_count, f):
    #prints line_count, then prints the next line in file f
    print(line_count, f.readline())

#declares a variable named current_file that holds the file whose name is stored in input_file
current_file = open(input_file)

#print "First let's print the whole file:" and enters to the next line
print("First let's print the whole file:\n")

#calls the function print_all and passes it an argument named current_file
print_all(current_file)

#print "Now let's rewind, kind of like a tape."
print("Now let's rewind, kind of like a tape.")

#calls the function rewind and passes it an argument named current_file
rewind(current_file)

#prints "Let's print three lines:"
print("Let's print three lines:")

#declares a variable named current_line holding the integer 1
current_line = 1
#calls the function print_a_line and passes it two arguments, current_line and current_file
print_a_line(current_line, current_file)

#adds one to the integer variable current_line
#now it's 2
current_line += 1
#calls the function print_a_line and passes it two arguments, current_line and current_file
print_a_line(current_line, current_file)

#adds one to the integer variable current_line
#now it's 3
current_line += 1
#calls the function print_a_line and passes it two arguments, current_line and current_file
print_a_line(current_line, current_file)
