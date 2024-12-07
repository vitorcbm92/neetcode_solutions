def factorial(num: int) -> int:
    if num < 0:
        return 0
    elif num == 0:
        return 1
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
            return factorial

if __name__ == '__main__':
    result = factorial(7)