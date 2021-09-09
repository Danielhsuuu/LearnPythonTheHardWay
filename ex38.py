
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there's not 10 things in that list, let's fix that.")
stuff = ten_things.split(' ') #split(ten_things, ' ') splits ten_things into segments separated by space
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() #removes the last item from the list more_stuff and stores the removed value in the variable next_one
    print("Adding: ", next_one)
    stuff.append(next_one) #appends variable next_one into the list more_stuff
    print("There's %d items now." % len(stuff))

print("There we go: ", stuff)

print("Let's do some things with stuff.")
print(stuff[1])
print(stuff[-1]) # whoa! fancy
print(stuff.pop()) #removes the last item from the list stuff and prints out the removed value
print(' '.join(stuff)) # what? cool! Join stuff with ‘ ‘ between them.
print('#'.join(stuff[3:5])) # super stellar! Join stuff that are index 3 to 5 with ‘ ‘ between them.

#1. Take each function that is called, and go through the steps outlined above to translate them to what Python does. For example, ' '.join(things) is join(' ', things).
#2. Translate these two ways to view the function calls. For example, ' '.join(things) reads as, “Join things with ‘ ‘ between them.” Meanwhile, join(' ', things) means, “Call join with ‘ ‘ and things.” Understand how they are really the same thing.
#5. What’s the relationship between dir(something) and the “class” of something?
    #dir(something) returns a list of the attributes and methods of class something