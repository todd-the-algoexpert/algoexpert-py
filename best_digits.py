def bestDigits(number, numDigits):
    if numDigits == 0:
        return number
    length = len(number)
    if length == numDigits:
        return ""
    if numDigits == 1:
        best_n = 0
        for i in range(length):
            n = int(number[:i] + number[i+1:])
            if n > best_n:
                best_n = n
        return str(best_n)
    required_length = length - numDigits
    while len(number) > required_length:
        number = bestDigits(number, 1)
    return number
