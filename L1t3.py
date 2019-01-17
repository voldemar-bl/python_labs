def is_triangle(a: float, b: float, c: float):
    return a + b > c and a + c > b and b + c > a


if __name__ == '__main__':
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

    if is_triangle(a, b, c):
        result = "triangle"

    else:
        result = "not triangle"
    print(result)
