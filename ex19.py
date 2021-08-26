#defines a functioin named cheese_and_crackers that takes two arguments named cheese_count and boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers): 
    #prints "You have {cheese_count} cheeses!"
    print("You have %d cheeses!" % cheese_count)
    #prints "You have {boxes of crakers} boxes of crakers!"
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    #prints "Man that's enough for a party"
    print("Man that's enough for a party!")
    #prints "Get a blanket." and return to the next line
    print("Get a blanket.\n")

#prints "We can just give the function numbers directly:"
print("We can just give the function numbers directly:")
#calls the function cheese_and_crackers and gives it 20 and 30 as arguments
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
#declares a variable named amount_of_cheese holding the integer 10
amount_of_cheese = 10
#declares a variable named amount_of_crackers holding the integer 50
amount_of_crackers = 50

#calls the function cheese_and_crackers and gives it amount_of_cheese and amount_of_crackers as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#prints "We can even do math inside too:"
print("We can even do math inside too:")
#calls the function cheese_and_crackers and gives it 10+20 and 5+6 as arguments
cheese_and_crackers(10 + 20, 5 + 6)
#prints "And we can combine the two, variables and math:"
print("And we can combine the two, variables and math:")
#calls the function cheese_and_crackers and gives it amount_of_cheese + 100 and amount_of_crackers + 1000 as arguments
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

#study drill
def plus(value1, value2):
    print(value1 + value2)

plus(1, 1)
plus(2, 2)
plus(3, 3)
plus(4, 4)
plus(5, 5)
plus(6, 6)
plus(7, 7)
plus(8, 8)
plus(9, 9)
plus(10, 10)