#we need the 'w' because open needs the explicit command to write stuff in out txt file
#we do not need the truncate funtion because writing things into the file has already emptied the file
from sys import argv

script, filename = argv
print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")
print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
#target.truncate()

print("Now I'm going to ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
whatToPrint = "{}\n{}\n{}\n"

print("I'm going to write these to the file.")
target.write(whatToPrint.format(line1,line2,line3))

print("And finally, we close it.")

target.close()