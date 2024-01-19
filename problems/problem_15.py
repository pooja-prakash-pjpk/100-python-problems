#
# Question 15:
#
# Write a program that computes the value of a+aa+aaa+aaaa
# with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

num = int(input("Enter any whole integer num between 1-9"))
num1 = ((num*10)+ num)
num2 = ((num1 *10)+ num)
num3 = ((num2*10)+num)
final_ans = num+num1+num2+num3
print(f'{num} + {num1} + {num2} + {num3} = {final_ans}')