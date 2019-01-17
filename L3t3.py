if __name__ == '__main__':
    n = int(input("n: "))
    s = 0
    s_i = 0
    for i in range(1, n):
        num = int(input("# "))

        s += num
        s_i += i

    result = s_i - s + n
    print(result)

