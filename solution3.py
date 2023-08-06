# Write a function that returns the nth elements in the Fibonacci Sequence.

def fibonacci(n):
    if n <= 0:
        print("incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

        fibonacci(n+n)