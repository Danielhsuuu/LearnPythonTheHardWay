#declares a variable named fruits containing int 10
fruits = 10

#declares an f-string containing "There are {fruits} types of fruits."
#a string inside a string
x = f"There are {fruits} types of fruits."

#declares a string named math containing "math"
math = "math"
#declares a string named do_not containging "don't"
do_not = "don't"

#declares an f-string containing "Those who know {math} and those who {do_not}."
#a string inside a string*2
y = f"Those who know {math} and those who {do_not}."

#prints x
print(x)
#prints y
print(y)

#prints I said: There are 10 types of fruits.
#a string inside a string
print(f"I said: {x}")
#prints I also said: 'Those who know math and those who don't.'
#a string inside a string
print(f"I also said: '{y}'")

#declares a boolean containing false
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

#prints Isn't that joke so funny?! math
print(joke_evaluation.format(math))

#declares a String containing "This is the left side of..."
w = "This is the left side of..."
#declares a String containing "a string with a right side."
e = "a string with a right side."

#prints This is the left side of...a string with a right side.
print(w + e)
#w + e makes a longer string because e is simply put behind w