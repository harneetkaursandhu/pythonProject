# The __init__ method is similar to constructors in C++ and Java. Constructors are used to initializing the object’s
# state. Like methods, a constructor also contains a collection of statements(i.e. instructions) that
# are executed at the time of Object creation. It runs as soon as an object of a class is instantiated.
# The method is useful to do any initialization you want to do with your object.

# Sample class with init method
class Person:

    # init method or constructor
    def __init__(self, name):
        self.name = name

    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)


p = Person('Nikhil')
p.say_hi()

# In this example, we are creating a Person class and we have created a name instance variable in the
# constructor. We have created a method named as say_hi() which returns the string
# “Hello, my name is {name}”.We have created a person class object and we pass the name
# Nikhil to the instance variable. Finally, we are calling the say_hi() of the class.
