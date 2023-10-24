# Parent class
class Animal:
    def speak(self):
        print("Animal is speaking")

# Child class Dog
class Dog(Animal):  # Dog should inherit from Animal
    def bark(self):
        print("Dog is barking")

# Child class Cat
class Cat(Animal):
    def meow(self):
        print("Cat is meowing")

d = Dog()  # Instantiate a Dog object
d.speak()   # Call the speak method on the Dog object

c = Cat()  # Instantiate a Cat object
c.speak()   # Call the speak method on the Cat object
