#raw_input gets input from the user and returns the data input by the user in a string.
#the ' meaning feet in the height must have a \ that comes before it because otherwise the String would end there
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