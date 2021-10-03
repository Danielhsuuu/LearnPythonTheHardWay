#The object class exists because almost everything in python is an object.
#You can't use a class like it's an object because a class is essentially a template and an object is a thing created from that template
#When functions are in the base class they can be overriden with functions with the same name
#Yes, an object can belong to two classes at the same time.
## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    def __init__(self):
        self.species = "blah"

    def hello(self):
        print("hi animal")

    def sayspecies(self, species):
        return (species)

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name
        self.teeth = [1,2,3,4,5]

    def hello(self):
        print("hi dog")

## Cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None
        self.relatives = [1,2,3]

    def hello(self):
        print("hi person")

## Employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ## run the __init__ method of a parent class reliably
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def getColor(self, color):
        return (color)

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

mary.hello()

## mary's pet is satan
mary.pet = satan

satan.hello()

print(rover.sayspecies(rover))

## frank is-a Employee, his salary is 120000
frank = Employee("Frank", 120000)

## frank's pet is rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish("flipper name", "blue")

## crouse is-a Salmon
crouse = Salmon("crouse name", "red")

## harry is-a Halibut
harry = Halibut("harry name", "green")

print(flipper.getColor(flipper))