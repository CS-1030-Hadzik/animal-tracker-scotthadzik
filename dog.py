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
        self.__age = 0 #private

    # getter
    def get_age(self):
        return self.__age
    
    # setter
    def set_age(self, new_age):
        if new_age < 0:
            return print("Age must be positive")
        self.__age = new_age

    def speak(self):
        print(f"{self.name} woofs")

    def trick(self, tricks):
        # sit, hold for food, play dead, shake, fetch, roll over
        # tricks = ("sit", "stay", "play dead", "shake", "fetch", "roll over")  

        print(f"{self.name}", end=" ")

        # switch statement
        match tricks:
            case "sit":
                print ("sits")
            case "stay":
                print ("stays in place")
            case "play dead":
                print("play dead on the ground")
            case "shake":
                print("shakes your hand")
            case "fetch":
                print("fetches the stick")
            case "roll over":
                print("rolls over on the ground")
            case _:
                print("That is not a trick")

    def __str__(self):
        return super().__str__() + f"Size: {self.size}\n"