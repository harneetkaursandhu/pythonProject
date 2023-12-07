# Concatenation - combining two or more strings into a single string

# To concatenate strings in Python use the "+" operator.
# "Hello " + "World" = "Hello World"
# "Hello " + "World" + "!" = "Hello World!"

string_1 = "Hello World"

print("Using the join method to add a : between every char...\n{0}"
      .format(":".join(string_1)),
      "\n")

print("Using the join method to add a whitespace between every char...\n{0}"
      .format(" ".join(string_1)),
      "\n")

