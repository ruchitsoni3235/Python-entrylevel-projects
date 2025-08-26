"""def shortest_word(s):
    words = s.split()
    if not words:
        return ""
    shortest = words[0]  #The first letter is small
    for word in words[1:]:
        if len(word) < len(shortest):
            shortest = word
    return shortest


print(shortest_word("I love python"))
"""


# shortest string using pythonic way

def shortest_string(s):
    words = s.split()
    return min(words, key=len) if words else ""


print(shortest_string("I love Python coding"))
