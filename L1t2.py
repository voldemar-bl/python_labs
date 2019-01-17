def sing(x: int, y: int):
    word: str = '-'.join(["la" for i in range(x)])
    song = ' '.join(([word] * y))

    return song


if __name__ == "__main__":
    x = int(input('x: '))
    y = int(input("y: "))
    z = int(input("z: "))

    song = sing(x, y)

    if z == 1:
        end = "!"
    else:
        end = "."

    if y > 0:
        space = ' '
    else:
        space = ''

    print("Everybody sing a song:" + space + song + end)
