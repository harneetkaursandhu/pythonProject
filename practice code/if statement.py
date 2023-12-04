# Do some research online and find out 5 interesting facts about New Zealand that you never knew.
# Make these into 5 quiz questions. These can be multiple choice, short answers or both.
# Use Python to create the quiz.
# At the end of the quiz, the user should be presented with their score.
# A good program will not be case sensitive.
# An excellent program will display the total time taken to complete the quiz.


from datetime import datetime

score = 0
start_time = datetime.today()

answer_one = (input("What is the capital of New Zealand?\n\n"))
if answer_one.lower() == "wellington":
    score = score + 1
    print("\nThat is correct. Your current score is ", score, "\n\n")
else:
    print("\nThat is incorrect. Your current score is still", score, "\n\n")
answer_two = (input("What is the Maori name for New Zealand?\n\n"))
if answer_two.lower() == "aotearoa":
    score = score + 1
    print("\nThat is correct. Your current score is ", score, "\n\n")
else:
    print("\nThat is incorrect. Your current score is still", score, "\n\n")
answer_three = (input("What is the name of the New Zealand Rubgy team?\n\n"))
if answer_three.lower() == "all blacks":
    score = score + 1
    print("\nThat is correct. Your current score is ", score, "\n\n")
else:
    print("\nThat is incorrect. Your current score is still", score, "\n\n")
answer_four = (input("The colours of the New zealand flag are red, blue and ?????\n\n"))
if answer_four.lower() == "white":
    score = score + 1
    print("\nThat is correct. Your current score is ", score, "\n\n")
else:
    print("\nThat is incorrect. Your current score is still", score, "\n\n")
answer_five = (input("what is the international dialing code for New Zealand?\n\n"))
if answer_five.lower() == "64":
    score = score + 1
    print("\nThat is correct. Your current score is ", score, "\n\n")
else:
    print("\nThat is incorrect. Your current score is still", score, "\n\n")
print("\nYour final score is ", score, "\n\n")
print("The time taken for you to complete this quiz is....", datetime.today() - start_time)
