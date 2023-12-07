# Creating an object in Python involves instantiating a class to create a new instance of that class.

class Dog:
    # A simple class
    # attribute
    attr1 = "mammal"
    attr2 = "dog"

    # A sample method
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)


# Driver code
# Object instantiation
Rodger = Dog()

# Accessing class attributes
# and method through objects
print(Rodger.attr1)
Rodger.fun()

# In this example, we are creating a Dog class and we have created two class variables attr1 and attr2.
# We have created a method named fun() which returns the string “I’m a, {attr1}” and I’m a, {attr2}.
# We have created an object of the Dog class and we are printing at the attr1 of the object.
# Finally, we are calling the fun() function.
