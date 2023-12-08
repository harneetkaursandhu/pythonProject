# The singleton pattern is a design pattern that ensures a class has only one instance and
# provides a global access point to that instance. This pattern is useful when only a single
# instance of a class is required to control the action throughout the execution.

# Here is an example of how the singleton pattern can be implemented in Python:

class Singleton:
    __instance = None

    def __new__(cls):
        if Singleton.__instance is None:
            Singleton.__instance = object.__new__(cls)
        return Singleton.__instance


s1 = Singleton()
s2 = Singleton()

print(s1 is s2)  # True

# In this example, the Singleton class has a class variable __instance that keeps track of the  single
# instance of the class. The __new__ method is overridden to check if an instance of the class already
# exists, if not it creates a new instance and stores it in the __instance variable. Any subsequent calls to
# the Singleton class will return the same instance stored in __instance, ensuring that only one instance of
# the class is ever created. In this example, creating two objects s1 and s2 using the Singleton
# class, and comparing them with is operator , returns True because they are the same instances.
