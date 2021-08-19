fruits = 10
x = f"There are {fruits} types of fruits."

math = "math"
do_not = "don't"
y = f"Those who know {math} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(math))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)