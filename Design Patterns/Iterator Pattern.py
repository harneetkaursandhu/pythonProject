# The iterator pattern is a design pattern that provides a way to access the elements of an
# aggregate object sequentially without exposing its underlying representation. It allows the client
# to traverse a collection of objects without the need to know the implementation details of
# the collection. This pattern is useful when you want to provide a consistent way to access and
# traverse a collection of objects, and it promotes loose coupling between the collection and the client.
# In Python, the iterator pattern can be implemented by creating an iterator class that implements
# the __iter__() and __next__() methods and using the iter() and next() built-in functions.

# Here is an example of how the iterator pattern can be implemented in Python:

class Iterator:
    def __init__(self, data):
        self._index = 0
        self._data = data

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._data):
            raise StopIteration()
        result = self._data[self._index]
        self._index += 1
        return result


class Aggregate:
    def __init__(self):
        self._data = [1, 2, 3, 4, 5]

    def create_iterator(self):
        return Iterator(self._data)


# Client code
aggregate = Aggregate()
iterator = aggregate.create_iterator()
for item in iterator:
    print(item)

# In this example, the Iterator class implements the iterator pattern by defining the __iter__()
# and __next__() methods. The Aggregate class represents the collection of objects and it has a
# create_iterator() method that returns an instance of the Iterator class. The client code creates
# an instance of the Aggregate class, then it creates an iterator and uses it to traverse the
# collection of objects by calling the next() function on it. The Iterator class keeps track of the
# current position in the collection, and it returns the next item in the collection with the
# __next__() method. If there are no more items in the collection, it raises a StopIteration
# exception. In this example, the client code creates an instance of the Aggregate class,
# then it creates an iterator by calling the create_iterator() method and uses a for loop to
# traverse the collection of objects by calling the next() function on it. The Iterator class
# keeps track of the current position in the collection, and it returns the next item in the
# collection with the __next__() method. The output of the code is 1, 2, 3, 4, 5
