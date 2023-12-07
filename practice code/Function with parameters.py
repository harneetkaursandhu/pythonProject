# Often it is necessary to pass data to a function. The syntax for this
# is shown in the example below.

def show_hello(param):
    print("Hello there, the number of times this "
          "function is called is {0}!!!\n\n".format(param))


# creating and setting a counter
counter = 0
print("Testing my second user defined function...\n\n")

counter += 1
# invoking the function
show_hello(counter)

counter += 1
# invoking the function again
show_hello(counter)

# The syntax for a function with a parameter uses the parameter name in parenthesis.
# This is referred to as the function or method signature. In our simple example,
# the function takes a single parameter (called param) and uses it to output the
# value in the string. To invoke the function, the correct signature
# (show_hello(<some int value>)) must be used. If not, then the interpreter will throw an error.
