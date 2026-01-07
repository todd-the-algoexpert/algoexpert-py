def reversePolishNotation(tokens):
    nums = []
    answer = 0
    for token in tokens:
        if token in "+-*/":
            n1 = int(nums.pop())
            n2 = int(nums.pop())
            if token == "+":
                nums.append(n1 + n2)
            elif token == "-":
                nums.append(n2 - n1)
            elif token == "*":
                nums.append(n1 * n2)
            else:
                nums.append(n2 / n1)
        else:
            nums.append(token)
    return int(nums.pop())
