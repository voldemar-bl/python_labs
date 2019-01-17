def super_fibonacci(n, m):
    if n > 0 and m <= 35 and m > 0:
        l = []
        while m != 0:
            l.append(1)
            m -= 1
        z_list = len(l) - 1
        while len(l) < n:
            l.append(sum(l[-1 - z_list:]))
        return l[-1]
    else: return "одно из чисел выходит за ограничения"


if __name__ == '__main__':
    print(super_fibonacci(-1, 1))
    print(super_fibonacci(3, 5))
    print(super_fibonacci(8, 2))
    print(super_fibonacci(9, 3))