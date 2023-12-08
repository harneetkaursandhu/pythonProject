# The factory pattern is a design pattern that provides an interface for creating objects in a super
# class, but allows subclasses to alter the type of objects that will be created. This pattern is useful
# when a class can’t anticipate the type of objects it must create, or when a class wants its subclasses
# to specify the objects it creates. In Python, the factory pattern can be implemented by creating a
# factory method or an abstract factory class that is responsible for creating objects.

# Here is an example of how the factory pattern can be implemented in Python:

class Dog:
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof!"


class Cat:
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow!"


def get_pet(pet="dog"):
    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))
    return pets[pet]


d = get_pet("dog")
print(d.speak())

c = get_pet("cat")
print(c.speak())

# In this example, the get_pet function acts as a factory method that creates Dog and Cat objects.
# It takes an optional parameter pet which specifies the type of object to create. If pet is not
# specified, it defaults to creating a Dog object. The factory method uses a dictionary to map pet
# types to their corresponding classes, and returns an instance of the appropriate class.
# In this example, when the get_pet("dog") is called it returns the instance of the Dog class and
# when get_pet("cat") is called it returns the instance of the Cat class.
