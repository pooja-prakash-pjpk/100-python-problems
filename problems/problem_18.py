# Question:
#
# A website requires the users to input username and password to register.
# Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# At least 1 letter between [a-z]
# At least 1 number between [0-9]
# At least 1 letter between [A-Z]
# At least 1 character from [$#@]
# Minimum length of transaction password: 6
# Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords
# and will check them according to the above criteria.
# Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1



def is_length(x):
    if 6 <= len(x) <= 12:
        return True
    else:
        return False



def is_upper(x):
    for i in x:
        if i.isupper():
            return True
    return False



def is_lower(x):
    for i in x:
        if i.islower():
            return True
    return False




def is_num(x):
    for i in x:
        if i.isdigit():
            return True
    return False



def is_special_char(x):
    for i in x:
        if i == '$' or i == '#' or i == '@':
            return True
    return False



password = input().split(',')
valid_password = []

for i in password:
    if is_num(i) and is_lower(i) and is_upper(i) and is_length(i) and is_special_char(i):
        valid_password.append(i)

    # print(f'{i}, Upper - {is_upper(i)}')
    # print(f'{i}, Lower - {is_lower(i)}')
    # print(f' {i}, Length {is_length(i)}')
    # print(f'{i}, is number - {is_num(i)}')
    # print(f'{i}, special _char {is_special_char(i)}')
print(valid_password)




