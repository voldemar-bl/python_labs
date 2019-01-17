def pal():
    word = input("check word: ").replace(" ", "").lower()

    if word == word[::-1]:
        return "yes"
    return "no"


if __name__ == '__main__':
    print(pal())
