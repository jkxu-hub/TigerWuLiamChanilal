class Animal:
    
    # constructor
    def __init__(self, age, gender, name):
        #fields
        self.age = age 
        self.gender = gender
        self.name = name

    #methods
    def take_damage(self, damage):
        self.health -= damage

    def __str__(self):
        return f"{self.name} is {self.age} and {self.gender} and has {self.health} health points"

a1 = Animal(6, "male", "Bob")
print(a1)
a1.take_damage(10)
print(a1)

# inheritance
class Dog(Animal):
    fur_color = "black"

    def __init__(self, age, gender, name, fur_color):
        super().__init__(age, gender, name)
        self.fur_color = fur_color
        
d1 = Dog(7, "male", "Bobo", "orange")
print(d1)
