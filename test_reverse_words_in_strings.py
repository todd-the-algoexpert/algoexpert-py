def reverse_words_in_strings(s):
    if s == '' or s is None:
        return s
    words = ''
    space = ' '
    i = 0
    current = s[i]
    i += 1
    is_ws = current.isspace()

    while i < len(s):
        c = s[i]
        i += 1
        if (is_ws and c == space) or (not is_ws and c != space):
            current += c
        else:
            words = current + words
            current = c
            is_ws = current.isspace()
    words = current + words
    return words


def test_nothing():
    assert reverse_words_in_strings('') == ''


def test_single_char():
    assert reverse_words_in_strings('c') == 'c'


def test_basic_sentence():
    assert reverse_words_in_strings("What is your name?") == "name? your is What"
