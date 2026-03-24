class Animal:
    """
    Base class representing a generic animal.
    """
    # Class level attribute
    kingdom = "Animalia" # Every object will have this attribute

    #object specific attributes
    # constructor -- initializer
    # dunder init magic method
    def __init__(self, name, species): # object attribute
        self.name = name
        self.species = species

    # class method
    def speak(self): # pass self error methods 0 argument expected 1
        print (f"{self.name} makes a noise")


    # overiding the print function to send a formatted string when print
    def __str__(self):
        return (f"Kingdom: {self.kingdom}\n"
                f"Name: {self.name}\n"
                f"Species: {self.species}\n")
 
