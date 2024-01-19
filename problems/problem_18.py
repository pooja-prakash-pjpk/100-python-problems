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


predicates = [is_num, is_upper, is_lower, is_length, is_special_char]


def validate_password(password):
    for predicate in predicates:

        if not predicate(password):
            return False
    return True


def find_valid_password(passwords):
    valid_passwords = []
    for password in passwords:
        if validate_password(password):
            valid_passwords.append(password)
    return valid_passwords


# print(find_valid_password(['ABd1234@1','a F1#','2w3E*','2We3345']))
print(find_valid_password(input().split(',')))
