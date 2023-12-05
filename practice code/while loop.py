# Write a program with a while loop that prints 1 through to n in square brackets. For example, if the user enters 6
# then the program should display
# [1] [2] [3] [4] [5] [6]

is_running = True
number = int(input("Please enter a number\n\n"))
counter = 0
while counter < number:
    print("[", counter + 1, "] ", end="")
    counter += 1
