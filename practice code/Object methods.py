# Objects can also have Methods. Methods are functions of objects.

# The following example shows how to create a method in the Person class:

class Person:

    def __init__(self, age, gender):
        self.age = age

        self.gender = gender

    def myIntro(self):
        print("Hello my gender is " + self.gender)
        print('Hello my age is', self.age)  # , is used when we need to show int or float values.


harry = Person(36, "male")

sarrah = Person(34, "female")

harry.myIntro()

sarrah.myIntro()

# You should pass values in object in same order as mentioned in _init() method.

# In the above example, first age will come, then gender.
