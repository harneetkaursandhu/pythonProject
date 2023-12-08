# The facade pattern is a design pattern that provides a simplified interface to a complex system of
# classes. It acts as an intermediary between the client and the system, hiding the complexity of
# the system and exposing only the necessary functionality to the client. This pattern is useful
# when you want to provide a simple and easy-to-use interface to a complex system of classes,
# and it promotes loose coupling between classes. In Python, the facade pattern can be implemented
# by creating a facade class that wraps the complex system of classes and exposes a simplified interface to the client.

# Here is an example of how the facade pattern can be implemented in Python:

class Subsystem1:
    def method1(self):
        print("Subsystem1 method1")


class Subsystem2:
    def method2(self):
        print("Subsystem2 method2")


class Facade:
    def __init__(self):
        self._subsystem1 = Subsystem1()
        self._subsystem2 = Subsystem2()

    def method(self):
        self._subsystem1.method1()
        self._subsystem2.method2()


# Client code
facade = Facade()
facade.method()

# In this example, the Subsystem1 and Subsystem2 classes define the complex functionality of the system.
# The Facade class provides a simplified interface to the client, it wraps the instances of the
# Subsystem1 and Subsystem2 classes and exposes a single method() that invokes the necessary methods
# of the subsystems. In this example, the client code creates an instance of the Facade class
# and calls the method() on it. The Facade class receives the request, and then it delegates
# the request to the appropriate methods of the Subsystem1 and Subsystem2 classes.
# The output of the code is “Subsystem1 method1” and “Subsystem2 method2”
