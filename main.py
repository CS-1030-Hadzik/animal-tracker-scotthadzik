from animal import Animal
from dog import Dog

if __name__ == "__main__":

    # kitty is an instance of the Animal class
    kitty = Animal("kitty", "feline")
    fido = Dog("Fido", "Canine", "Bulldog")

    print (kitty)
    print (fido)
    kitty.speak()
    fido.speak()
    # TODO: Print the Animal instance
    # TODO: Call the method to make a generic animal sound

    # TODO: Create an instance of the Dog class
    # TODO: Print the Dog instance
    # TODO: Call the method to make the dog-specific sound

    # TODO print out all the animals
