# Inheritance / Arv: A class can inherit attributes and methods from another class.

class Animal:# All base classes inhertis from the basic Object type
    def __init__(self, name, legs=0):
        self.name = name
        self.legs = legs

    def speak(self, animal_sound=""):
        print("Some random animal sound")
    
    def describe(self):
        print(f"{self.name} has {self.legs} legs")



class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, 4) # This calls on the parent/super Class __init__ and defines that dog should have 4 legs
    def speak(self):
        print(f"{self.name} says: Woof")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Mjau")

class Fish(Animal):
    #Fish should have 0 legs
    def __init__(self, name):
        super().__init__(name, 0)
    
    def speak(self):
        print(f"{self.name} says blubblubblub")
    
        

some_animal = Animal("Rogers")
dog = Dog("Buddy")
cat = Cat("Whiskers")
fish = Fish("Blubbel")

dog.speak()
cat.speak()
some_animal.speak()
fish.speak()
dog.describe()

