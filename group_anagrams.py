def count_chars(string, char):
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count

def anagram(word, letters):
    if len(word) != len(letters):
        return False
    for c in word:
        letters_count = count_chars(letters, c)
        word_count = count_chars(word, c)
        if letters_count != word_count:
            return False
    
    return True

def groupAnagrams(words):
    anagrams = []
    i = 0
    while i < len(words): 
        current = words[i]
        a = [current]
        j = i + 1
        while j < len(words):
            if anagram(current, words[j]):
                a.append(words[j])
                del words[j]
            else:
                j += 1
        anagrams.append(a)
        i += 1
    return anagrams
