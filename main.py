from animal import Animal
from dog import Dog

if __name__ == "__main__":

    #object of the animal class instance of the animal class. Intanciation the class
    animal1 = Animal("Gus", "Mouse")
    dog2 = Dog("Nala", "Canine", "Medium")

    print(animal1)
    animal1.speak()

    print(dog2)
    dog2.speak()

    # TODO print out all the animals
