# Question16 :

# Use a list comprehension to square each odd number in a list.
# The list is input by a sequence of comma-separated numbers.
# >Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,9,25,49,81

list1 = [12, 13, 14, 15, 16, 17]
new_list = []
new_list = list(filter(lambda item: item % 2 != 0, list1))
print(list(map(lambda item: item * item, new_list)))
