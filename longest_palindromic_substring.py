def longestPalindromicSubstring(string):
    pal = string[0:1]
    length = len(string)
    for i in range(0, length - 1):
        for j in range(i + 1, length + 1):
            candidate = string[i:j]
            reversed = candidate[::-1]
            if candidate == reversed and len(candidate) > len(pal):
                pal = candidate    
    return pal
