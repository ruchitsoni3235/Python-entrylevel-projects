def most_freq(s):
    char_count = {}

    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    max_char = ""
    max_count = 0

    for char, count in char_count.items():
        if count > max_count:
            max_char = char
            max_count = count
    return max_count, max_char


print(most_freq("javascript"))
