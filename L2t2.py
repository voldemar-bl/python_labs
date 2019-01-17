def esrever_gnirts(string: str):
    string = " ".join(reversed(string.split(" ")))
    if string.endswith(" "):string = string[:-1]
    return string


if __name__ == '__main__':
    string = input("string: ")

    print(esrever_gnirts(string))
