# Question 5:
#
# Define a class which has at least two methods:
#
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
# Hints:
#
# Use init method to construct some parameters

class TestString():
    def __init__(self):
        self.s = ""
        pass

    def getString(self):
        self.s = input("enter string ")
        return

    def printString(self):
        print(self.s.upper())
        return


str_obj = TestString()
str_obj.getString()
str_obj.printString()
