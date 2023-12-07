# Write a program that reads a wavelength from the user and reports its colour.

# Display an appropriate error message if the wavelength entered by the user is outside of the
# visible spectrum.

print("Welcome to wavelength to colour converter\n")
wave_length = int(input("Please enter an integer wavelength between 380 and 750\n"))
print("Thank you, the wavelength that you entered in nanometres is ", wave_length, "\n")
print("The colour for this wavelength is...", end="")

if wave_length > 750:
    print("The wavelength entered is higher than the visible spectrum! This is infrared.")
elif wave_length >= 620:
    print("Red")
elif wave_length >= 590:
    print("Orange")
elif wave_length >= 570:
    print("Yellow")
elif wave_length >= 495:
    print("Green")
elif wave_length >= 450:
    print("Blue")
elif wave_length >= 380:
    print("Violet")
else:
    print("Indeterminate, :-(, the number entered is "
          "outside the visible spectrum!")

#  The program works by checking the boolean conditions.
#
# When a condition is met, the appropriate actions are performed, and the rest of the if statement is skipped.
#
# This is important. It means that the order of the variables being evaluated must run from highest to lowest.

# An other point to note is that the final else clause should always contain an error message.
