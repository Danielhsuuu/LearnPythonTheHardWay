#pydoc extracts documentation from the source code itself
#raw_input doesn't work, so I used input
age = input("how old are you?")
height = input("how tall are you?")
weight = input("how much do you weigh?")
gpa = input("What's your gpa?")

print("so you are %r old, %r tall, and %r heavy." % (age, height, weight))