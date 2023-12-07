# Write a program with a while loop that prints 1 through to n in square brackets. For example, if the user enters 6
# then the program should display
# [1] [2] [3] [4] [5] [6]


number = int(input("Please enter a number\n\n"))
counter = 0
while counter < number:
    print("[", counter + 1, "] ", end="")
    counter += 1

# For a While code block to start, the < boolean condition > must be True. The interpreter will
# execute actions in the code block until the same boolean condition becomes False.
# In this program the user will enter any number. The value of counter is set to 0. The program will
# continue to run until the value of counter is less than the number entered
