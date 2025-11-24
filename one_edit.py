def remove_char_at(s, i):
    result = s[:i] + s[i + 1:]
    print(result)  # Output: exmple
    return result


def oneEdit(stringOne, stringTwo):
    length1 = len(stringOne)
    length2 = len(stringTwo)
    print(f"{length1} and {length2}")
    if length1 + 1 < length2 or length2 + 1 < length1:
        return False
    if stringOne == stringTwo:
        return True
    if length1 + 1 == length2:
        for i in range(length2):
            trimmed = remove_char_at(stringTwo, i)
            print(f"{trimmed} and {stringOne}")
            if stringOne == trimmed:
                return True
                
    if length2 + 1 == length1:
        for i in range(length1):
            trimmed = remove_char_at(stringOne, i)
            print(f"{trimmed} and {stringTwo}")
            if stringTwo == trimmed:
                return True

    if length1 == length2:
        for i in range(length1):
            trim1 = remove_char_at(stringOne, i)
            trim2 = remove_char_at(stringTwo, i)
            if trim1 == trim2:
                return True
    
    return False
