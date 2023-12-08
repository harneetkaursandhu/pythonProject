# The observer pattern is a design pattern that allows an object (the subject) to notify
# other objects (the observers) of any changes to its state. This pattern is useful when multiple
# objects need to be notified of changes to another object, and it promotes loose coupling between
# objects. In Python, the observer pattern can be implemented using the built-in abc module which
# provides the ABC and abstractmethod decorators for creating abstract base classes (ABCs) and
# abstract methods.

# Here is an example of how the observer pattern can be implemented in Python:

from abc import ABC, abstractmethod


class Subject(ABC):
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()

    @abstractmethod
    def get_state(self):
        pass

    @abstractmethod
    def set_state(self, state):
        pass


class ConcreteSubject(Subject):
    def __init__(self):
        super().__init__()
        self._state = None

    def get_state(self):
        return self._state

    def set_state(self, state):
        self._state = state
        self.notify()


class Observer(ABC):
    @abstractmethod
    def update(self):
        pass


class ConcreteObserver(Observer):
    def __init__(self, subject):
        self._subject = subject
        self._subject.attach(self)

    def update(self):
        print(f'Observer: {self} has state {self._subject.get_state()}')


s = ConcreteSubject()
o1 = ConcreteObserver(s)
o2 = ConcreteObserver(s)

s.set_state(0)
s.set_state(1)

# In this example, the Subject class defines the interface for notifying observers, the ConcreteSubject
# class is a specific implementation of the subject that holds a state and notifies the observers
# when its state changes. The Observer class defines the interface for updating the observer,
# the ConcreteObserver class is a specific implementation of the observer that holds a reference
# to the subject and prints the current state of the subject when it is notified. The subject has
# a list of observers, which it notifies when its state changes. Each observer has a reference to
# the subject, and when it is notified, it updates its own state based on the subject’s state.
# In this example, when the state of the subject changes, it notifies the observer and
# the observer prints the current state of the subject.
