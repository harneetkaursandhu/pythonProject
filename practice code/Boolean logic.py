# I run a small grammar school in Auckland. I need a program that lets me know whether a student can enroll in our
# school. There are some conditions that must be met for each application.

# The program must check that the student:

# ·         Lives less than 4 km from the school

# ·         Is under 18 years old

# ·         Has the right to stay in New Zealand

# However, if a student is under 18, and will pay international student fees, then they can enroll.

print("This program works out eligibility for Secondary School enrolment....\n")
print("Student should be 10 to 18 year old ")
distance_from_school = float(input('Enter Distance in Kilometers: '))
age_in_years = int(input('Enter Student age: '))
has_residency = True
is_fee_foreign = False
print("The student's eligibility to enrol is ",
      distance_from_school < 4
      and 18 > age_in_years > 10
      and has_residency
      or 18 > age_in_years > 10
      and is_fee_foreign, "\n")

# When 2 or more bool variables are joined together, they always return a boolean (True or False).
# There is no other value returned such as "null" or "maybe". When the Python "and" operator is used,
# the variables on either side of the operator are checked. If either of the values are False,
# then operator returns False. If both the variables are True, then the operator returns True.

# The Python "or" operator is used to check if either of the variables is True. If a value is True,
# then the operator returns True. If both of the variables are False, then the operator returns False.

