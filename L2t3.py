def evaulate(str):
    stack = []
    str = str.replace('"', '')
    push_chars, pop_chars = "(", ")"
    for c in str:
        if c in push_chars:
            stack.append(c)
        elif c in pop_chars:
            if not len(stack):
                return False
            else:
                stack_top = stack.pop()
                balancing_bracket = push_chars[pop_chars.index(c)]
                if stack_top != balancing_bracket:
                    return False
    return not len(stack)


if __name__ == '__main__':
    if evaulate(str(input("type: "))):
        print("yes")
    else:
        print("no")
