def balancedBrackets(string):
    stack = []

    for c in string:
        if c in "([{":
            stack.append(c)
        elif c in "}])":
            if len(stack) == 0:
                return False
            e = stack.pop()
            if e == '(' and c != ')':
                return False
            if e == '[' and c != ']':
                return False
            if e == '{' and c != '}':
                return False
            
    return len(stack) == 0
