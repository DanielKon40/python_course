# Fibonacci sequence calculator

n = int(input("give me a number: "))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or  n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print(fibonacci(n))
