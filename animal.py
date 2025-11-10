class Animal:
    """
    Base class representing a generic animal.
    """
    # Class-level attribute
    kingdom = "Animalia"
    # TODO create a class-level attribute that is a list of all the Animal objects
    
    def __init__(self, name, species):
        self.name = name
        self.species = species

    # method is a way to do something with the class
    def speak(self):
        print("The animal makes a noise.")

    def __str__(self):
        return f"Kingdom: {self.kingdom}, Name: {self.name} Species: {self.species}"