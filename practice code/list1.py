# Write a program that displays the first 2 lists. The user must be prompted and given a choice
# to see either the sum or the average of the combined lists. Assume that the user enters valid integers only.

list_1 = [23, 66, 23, 12]
list_2 = [1, 19, 4, 8]
list_sum = (sum(list_1) + sum(list_2))
user_input = input("Type Sum or Average.\n\n")
if user_input.lower() == "sum":
    print("\nThe sum of the items in the list is.... ", list_sum)
if user_input.lower() == "average":
    average = float(list_sum) / (len(list_1) + len(list_2))
    print("\nThe average of the items in the list is.... ", average)
