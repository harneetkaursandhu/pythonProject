# Improved Calculator Example

def do_calculation(user_input):
    # variable to store result
    calculated_answer = int

    # split the input
    split_input = user_input.split()

    # get the parameters from split_input
    input_params = split_input[1].split(",")

    # do if elif
    if split_input[0] == "add":
        calculated_answer = int(input_params[0]) + int(input_params[1])
    elif split_input[0] == "subtract":
        calculated_answer = int(input_params[0]) - int(input_params[1])
    else:
        return "Unknown command entered!"
    return calculated_answer


# program run code

# getting the input
user_input = input("Please enter an operation and 2 parameters...\n")
# do calculation and display output
print("The answer is: {0}".format(do_calculation(user_input)),
      "\n")

# test case assertion 1
print("Assertion 1: 6 add 12 should be 18...\n")
print("The answer is: {0}".format(do_calculation("add 6,12")),
      "\n")

# test case assertion 2
print("Assertion 2: 626 subtract 100 should be 526...\n")
print("The answer is: {0}".format(do_calculation("subtract 626,100")),
      "\n")

# test case assertion 3
print("Assertion 3: 54 plus 8 should be Unknown command entered!...\n")
print(do_calculation("plus 54,8"),
      "\n")

# Notice, in the above example, that a function has been used to carry out the calculation.

# In keeping with best practice, the function returns a string, that can be displayed by calling
# code. This allows some separation of logic and presentation.

# The program uses 3 test case assertions that test each clause of the elif statement.

# The do calculation ( ) function is used in each test case.
