from animal import Animal
from dog import Dog


if __name__ == "__main__":

    # instance of the animal class -- instatiation
    # the object
    animal1 = Animal("Gus", "Mouse")
    
    dog2 = Dog("Nala", "Canine", "medium")

    print(animal1) # polymorphism
    animal1.speak() # Animal object "Gus makes a noise" polymorphism

    print(dog2)
    dog2.speak()  # Dog object "Nala woofs" polymorphism
    dog2.trick("stay")
    print(dog2.species) # public attribute
    print(dog2.get_age()) # private attribute

    dog2.set_age(-2)
    print(dog2.get_age()) # private attribute
    dog2.set_age(5)
    print(dog2.get_age())

    # TODO: Create an instance of the Dog class
    # TODO: Print the Dog instance
    # TODO: Call the method to make the dog-specific sound

    # TODO print out all the animals
