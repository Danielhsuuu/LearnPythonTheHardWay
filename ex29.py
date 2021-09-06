#the codes under if is run only when the condition behind if is met
#the code under if must be indented so that the compiler knows when the if ends
#if the codes aren't indented, the file can not be run. This is becuase there must be something under the if for the if to exist
#You can
#The conditions that were met may now be not met. The conditions that were not met may now be met. The corresponding codes will be run
people = 20 
cats = 30 
dogs = 15

if people < cats:
    print("Too many cats! The world is doomed!")
if people > cats:
    print("Not many cats! The world is saved!")
if people < dogs:
    print("The world is drooled on!")
if people > dogs:
    print("The world is dry!")

dogs += 5
if people >= dogs:
    print("People are greater than or equal to dogs.")
if people <= dogs:
    print("People are less than or equal to dogs.")
if people == dogs:
    print("People are dogs.")