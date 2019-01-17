
def crypto(str):
    KEY = 'aaaaabbbbbabbbaabbababbaaababaab'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_letter = ''
    str = str.replace(' ', '')
    ab = ""
    for letter in str:
        if letter.islower():
            ab += 'a'
        else:
            ab += 'b'

    d = len(ab)
    # print(ab)
    for i in range(0, d, 5):
        part = ab[i:i + 5]
        if len(part) == 5:
            # print(KEY.find(part))
            # print(part)
            new_letter += alphabet[KEY.find(part)]
    return new_letter


if __name__ == "__main__":
    print(crypto(input("decrypt: ")))
