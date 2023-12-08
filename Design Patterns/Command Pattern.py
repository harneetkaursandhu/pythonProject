# The command pattern is a design pattern that encapsulates a request or an action as an
# object, separating the command from the object that invokes it. This pattern is useful when you
# want to parametrize objects with different requests, delay or queue a request’s execution,
# and support undo/redo. In Python, the command pattern can be implemented by creating an interface
# for command objects and classes that implement that interface.
from abc import ABC, abstractmethod


# Here is an example of how the command pattern can be implemented in Python:

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class ConcreteCommand(Command):
    def __init__(self, receiver, value):
        self._receiver = receiver
        self._value = value

    def execute(self):
        self._receiver.action(self._value)


class Receiver:
    def action(self, value):
        print(f"Receiver action with value: {value}")


class Invoker:
    def __init__(self):
        self._commands = []

    def store_command(self, command):
        self._commands.append(command)

    def execute_commands(self):
        for command in self._commands:
            command.execute()


# Client code
receiver = Receiver()
command = ConcreteCommand(receiver, "Hello")
invoker = Invoker()
invoker.store_command(command)
invoker.execute_commands()

# In this example, the Command class defines the interface for command objects and the ConcreteCommand
# class is a specific implementation of the command that holds a reference to the Receiver object
# and the value it should operate on. The Receiver class defines the action that the command will
# invoke. The Invoker class holds a list of commands and can execute them. In this example,
# the client code creates a Receiver object, a ConcreteCommand object that’s associated with
# the Receiver and a value, and an Invoker object. It stores the command in the invoker, and
# then it invokes it. The command’s execute method is called which in turn calls the
# Receiver’s action method with the value passed in the ConcreteCommand’s constructor.
# The output of the code is Receiver action with value: Hello
