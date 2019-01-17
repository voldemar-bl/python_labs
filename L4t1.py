from collections import OrderedDict


def clean_list(list_to_clean):
    return list(OrderedDict.fromkeys(list_to_clean))


if __name__ == '__main__':
    list_clean = list(map(str, input().split(', ')))
    print(clean_list(list_clean))
