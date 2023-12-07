# Here is a simple example showing a function that returns data.


score = 4


def get_new_score(param_score):
    param_score += 1
    print("You got another point...\n"
          "Your score is now {0}.\n"
          .format(param_score))
    return param_score


# some run code
x = input("Your score is {0} points...\n\n"
          "Hit any key to get another point. "
          .format(score))
# invoking the function and using it to set the new score
score = get_new_score(score)
# test case assertion
# '''
print("Test case assertion: the current score is 5 "
      "and it should become 6!!")
# invoking the function
score = get_new_score(score)

# the current score is passed to the function as a parameter (param_score)
# and the value is incremented.
# At the end of the function, the new value of score is passed out using the return statement
# It is a programming convention in most OOP languages to include the word "get" in any function
# that uses a return statement.
