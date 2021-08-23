#raw_input doesn't work, so I used input
print("how old are you?", end = " ")
age = input()
print("how tall are you?", end = " ")
height = input()
print("how much do you weigh?", end = " ")
weight = input()
print("What's your gpa?", end = " ")
gpa = input()

print("so you are %r old, %r tall, and %r heavy." % (age, height, weight))