from animal import Animal
# Inheritance 

# child class - derived class
class Dog(Animal):
    """
    Derived class representing a dog, which is a type of Animal.
    """
    def __init__(self, name, species, size):
        super().__init__(name, species)
        self.size = size

    def speak(self):
        print(f"{self.name} woofs")
    
    def __str__(self):
        return super().__str__() + f"Size: {self.size}\n"