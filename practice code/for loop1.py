# "Write a program that will ask the user for a message and the number of times they want
# that message displayed. Then output the message that number of times."

user_input = int(input("Please enter the number of times "
                       "that you wish to see the message."))

for i in range(user_input):
    print("hello world....", i)
