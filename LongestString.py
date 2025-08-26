"""def longest_word(s):
    words = s.split()
    longest = ""  # empty string
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


print(longest_word("I love python programming"))"""


def longest_string(s):
    words = s.split()
    return max(words, key=len) if words else ""


print(longest_string("I love Python coding"))
