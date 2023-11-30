# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
Cats = 5
Dogs = 10
print(Cats)
print(Dogs)
print(Dogs + Cats)

x = 10
y = 2465511454663471
z = -3255522

print(type(x))

print(type(y))

print(type(z))

x = 5.2
y = -105.06

z= 12e3
print(type(x))
print(type(y))
print(type(z))

my_string = "Aoteroa - The Land of the Long Cloud."
print(my_string)

my_score = 201

print("The type of my_score is ", type(my_score), "\n")
print("my_score is ", my_score, "\n")

my_score = str(my_score)

print("The type of my_score is now ", type(my_score), "\n")
print("my_score is ", my_score,"\n")

print ("Welcome to your first data entry program\n")
user_name = input("Please enter your name...\n")
user_yob = int(input("Please enter your year of birth...\n"))
print("Thank you for your input\n")
print("The name that you entered is ", user_name)
print("Your age in years is ", 2016 - user_yob)

is_alive = True
time_remaining = False

# Test case assertion 1: result should be False
print("The game in progress status is....\n")
print(is_alive
      and time_remaining, "\n")