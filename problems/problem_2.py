# 2. Write a program which can compute the factorial of a given numbers.The results should
# be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output should be:40320 i.e 8*7*6..*1

def factorial(num):
    if num == 0:
        return 1

    answer = 1
    for i in range(1, num + 1):
        answer = answer * i
    return answer


if __name__ == '__main__':
    n = 5
    print(f"Factorial of {n}: {factorial(n)}")
