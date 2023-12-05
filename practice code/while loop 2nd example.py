# Write a program with a while loop that computes the sum of the first n positive integers:
#     sum = 1 + 2 + 3 + ... + n

number = int(input("Please enter a number\n\n"))
counter = 0
total = 0
while counter <= number:
    total = total + counter
    counter += 1
print("\nn = ", number, " sum = ", total, "\n\n")
