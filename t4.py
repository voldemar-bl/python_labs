from math import sqrt


def fibo(n: int):
    return int(((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5)))


if __name__ == '__main__':
    n = int(input("n: "))
    result = fibo(n)
    print(result)
