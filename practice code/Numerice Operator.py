# Program that lets me enter dimensions for the following compound shape and then outputs the area.

#  getting user inputs

a = int(input("Please enter the length of a\n"))
b = int(input("Please enter the length of b\n"))

# working out the 2 parts
total_area = b * a + a ** 2

print("The area of your shape is ", total_area, "\n")
