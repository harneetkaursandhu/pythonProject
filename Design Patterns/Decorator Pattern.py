# The decorator pattern is a design pattern that allows behavior to be added to an individual
# object, either statically or dynamically, without affecting the behavior of other objects
# from the same class. This pattern is useful when you want to add new functionality to an existing
# class without modifying its code. In Python, the decorator pattern can be implemented using
# decorators, which are special kind of functions that can be applied to other functions or
# classes to modify their behavior.

# Here is an example of how the decorator pattern can be implemented in Python:

class Component:
    def operation(self):
        pass


class ConcreteComponent(Component):
    def operation(self):
        return "ConcreteComponent"


class Decorator(Component):
    def __init__(self, component):
        self._component = component

    def operation(self):
        return self._component.operation()


class ConcreteDecoratorA(Decorator):
    def operation(self):
        return f"ConcreteDecoratorA({self._component.operation()})"


class ConcreteDecoratorB(Decorator):
    def operation(self):
        return f"ConcreteDecoratorB({self._component.operation()})"


# Client code
component = ConcreteComponent()
decoratorA = ConcreteDecoratorA(component)
decoratorB = ConcreteDecoratorB(decoratorA)
print(decoratorB.operation())

# In this example, the Component class defines the interface for objects that can have behavior
# added to them, the ConcreteComponent class is a specific implementation of the component that
# has some behavior. The Decorator class is an abstract class that implements the Component
# interface and has a reference to a Component object. The ConcreteDecoratorA and ConcreteDecoratorB
# classes are specific implementations of the Decorator class that add new behavior to the
# Component they decorate. The decorator classes are applied to the Component in a nested
# fashion, with each decorator wrapping the previous one. The operation() method is
# called on the outermost decorator and it returns the result of the operation() method
# of the innermost decorator, concatenated with the name of the decorator class.
# In this example, the ConcreteDecoratorB class is applied to the ConcreteDecoratorA,
# and the ConcreteDecoratorA is applied to the ConcreteComponent class, so the output
# of the decoratorB.operation() is ConcreteDecoratorB(ConcreteDecoratorA(ConcreteComponent))
