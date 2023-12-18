# Question 4:

# Write a program which accepts a sequence of comma-separated numbers from console and
# generate a list and a tuple which contains every number.Suppose the following input
# is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

def list_tuple_creator(*args):
    my_list = []
    my_tuple = ()
    for i in args:
        my_list.append(str(i))
    my_tuple = tuple(my_list)
    print(my_list)
    print(my_tuple)


list_tuple_creator(34, 67, 55, 33, 12, 98)
