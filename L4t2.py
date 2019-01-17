
def counter(a: int, b: int):
    a = a; b = b
    if a < 0 or b < 0:
        return "can't be negative"
    else:
        a_set: set = set(str(a))
        b_set: set = set(str(b))
        return len(a_set.intersection(b_set))


if __name__ == '__main__':
    var1, var2 = [int(x) for x in input("Enter two numbers here: ").split(",")]
    print(counter(var1, var2))
