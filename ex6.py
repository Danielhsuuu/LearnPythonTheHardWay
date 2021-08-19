#declares a variable named fruits containing int 10
fruits = 10

#declares an f-string containing "There are {fruits} types of fruits."
x = f"There are {fruits} types of fruits."

#declares a string named math containing "math"
math = "math"
#declares a string named do_not containging "don't"
do_not = "don't"

#declares an f-string containing "Those who know {math} and those who {do_not}."
y = f"Those who know {math} and those who {do_not}."

#prints x
print(x)
#prints y
print(y)

#prints I said: There are 10 types of fruits.
print(f"I said: {x}")
#prints I also said: 'Those who know math and those who don't.'
print(f"I also said: '{y}'")

#declares a boolean containing false
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(math))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)