# The manager of a bar needs an application to help door staff vet the patrons. The application must
# meet the following requirements:

# It prompts the user to enter the patron's year of birth and then their name
# If the person is less than 21 years old, then the application returns False
# The following patrons are not welcome at the bar:
# Suzanne May
# Wire-mu Range
# If these names are entered the application must return False.

from datetime import date

year_of_birth = input("\nPlease enter your year of birth: ")
name = input("Please enter your name: ")
current_year = date.today().year
print("\nThe result of your application is",
      str((current_year - int(year_of_birth) >= 21)
          and name != "Suzanne May"
          and name != "Wiremu Rangi"), ".")

# This example used the greater than or equal to operator ">=" to check the age of the person and
#  not operator is used to indicate that persons with the above names mentioned are not allowed in the bar.
