# Question 9:
# Write a program that accepts sequence of lines as input and prints the
# lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

content = []
while True:
    line = input("Enter Sequence of lines ")
    if line:
        content.append(line.upper())
    else:
        break
text = '\n'.join(content)
print(text)