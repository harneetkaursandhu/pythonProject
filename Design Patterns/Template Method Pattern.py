# The template method pattern is a design pattern that defines the skeleton of an algorithm in a
# method, and allowing subclasses to fill in the details. It provides a way to define the basic
# steps of an algorithm, and then allows subclasses to provide their own implementation for one
# or more of those steps. This pattern is useful when you want to define the skeleton of an algorithm,
# but you want to allow subclasses to provide their own implementation for some of the steps, and
# it promotes code reuse. In Python, the template method pattern can be implemented by creating a base class that
# defines the template method, and then creating subclasses that override one or more of the steps of the algorithm.

# Here is an example of how the template method pattern can be implemented in Python:

class AbstractClass:
    def template_method(self):
        self._step1()
        self._step2()

    def _step1(self):
        pass

    def _step2(self):
        pass


class ConcreteClass(AbstractClass):
    def _step1(self):
        print("ConcreteClass step1")

    def _step2(self):
        print("ConcreteClass step2")


# Client code
concrete = ConcreteClass()
concrete.template_method()

# In this example, the AbstractClass defines the template method, template_method() which calls
# the two steps of the algorithm, _step1() and _step2(). These methods are defined as abstract
# method so it can be implemented by the subclass. The ConcreteClass is a subclass of AbstractClass
# which provides the implementation for the two steps of the algorithm. The template_method() can
# be used as is, and it calls the two steps of the algorithm in the correct order. The client code
# creates an instance of the ConcreteClass and calls the template_method() on it. The ConcreteClass
# receives the request, and then it executes the two steps of the algorithm by calling the _step1()
# and _step2() methods. The output of the code is “ConcreteClass step1” and “ConcreteClass step2”
