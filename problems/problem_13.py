# problem 13
# Write a program that accepts a sentence and calculate
# the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3
sentence = input("Enter the sentence")
digits = 0
letters = 0
for i in sentence:
    if i.isalpha():
        letters = letters +1
    if i.isdigit():
        digits = digits+1

print(f'Letters : {letters} Digits : {digits}')
