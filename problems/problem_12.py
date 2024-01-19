# Question 12
# Write a program, which will find all such numbers between 1000 and 3000
# (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence
# on a single line.
# Hints:
#
# In case of input data being supplied to the question, it should be assumed
# # to be a console input.

def get_total_even(range1, range2):
    new_list = []
    for i in range(range1, range2 + 1):
        num_str = str(i)
        length = len(num_str)
        every_digit_even = True
        for j in range(0, length):
            if (int(num_str[j]) % 2) != 0:
                every_digit_even = False
                break
        if every_digit_even:
            new_list.append(i)

    print(new_list)


get_total_even(1000, 3000)
