# First code snippet
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()  # This print() is inside the while loop
fib(10)


if (5 > 2):
    print("Five is greater than two!")