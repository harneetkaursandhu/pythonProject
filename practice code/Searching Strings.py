# There are several ways to search a string to find stored information, even if it is in a long list of data.

string_1 = "here is a translation: Haera mai ki konei means come here!"

print("The number of times that k appears is {0}\n"
      .format(string_1.count("k")))

konei_endindex = string_1.find("konei") + len("konei")
print("The end index position of konei is {0}\n"
      .format(konei_endindex))

here_position = string_1.find("here", konei_endindex, len(string_1))
print("Looking for the string_1 here, anytime after konei...\n\n"
      "The string_1 here appears at index position..{0}"
      .format(here_position))

# The find( ) function in Python is overloaded. It can take just one parameter (shown on line 8)
# or 3 parameters (shown on line 12).
# Find( ) is a very useful means for searching strings. It returns the index integer of the item
# being searched for. If the function cannot find a matching string, then it returns -1.
# The find( ) syntax is:
#
# <string being searched>.find(<string to search for>, <start index>, <end index>)
