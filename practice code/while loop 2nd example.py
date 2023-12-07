# Write a program with a while loop that computes the sum of the first n positive integers:
#     sum = 1 + 2 + 3 + ... + n

number = int(input("Please enter a number\n\n"))
counter = 0
total = 0
while counter <= number:
    total = total + counter
    counter += 1
print("\nn = ", number, " sum = ", total, "\n\n")

# For a While code block to start, the < boolean condition > must be True. The interpreter will
# execute actions in the code block until the same boolean condition becomes False.
# The value of counter and total is set to 0. When the user will enter a number, the program will
# continue to run until the value of counter is less than or equal to the number entered. In every iteration the
# the value of counter will be incremented by 1 and will be added to the total and in the end the value of total will
# be printed.
