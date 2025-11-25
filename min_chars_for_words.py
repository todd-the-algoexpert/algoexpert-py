def minimumCharactersForWords(words):
    letters = {}
    for word in words:
        chars = {}
        for char in word:
            if char not in chars:
                chars[char] = 1
            else:
                chars[char] = chars[char] + 1
        for key, value in chars.items():
            if key not in letters:
                letters[key] = value
            else:
                current = letters[key]
                if current < value:
                    letters[key] = value
    print(letters)
    answer = []
    for key, value in letters.items():
        for i in range(value):
            answer += key
    
    # Write your code here.
    return answer
