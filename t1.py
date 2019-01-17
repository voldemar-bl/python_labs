from math import sqrt, pi, exp


def calc(a: float, b: float, c: float):
    result = (1.0 /
              (c * sqrt(2.0 * pi))) * exp(-(pow(a - b, 2.0) / 2.0 * pow(c, 2.0)))
    return result


if __name__ == '__main__':
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    print("Calculated number = ", calc(a, b, c))
