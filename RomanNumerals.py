def roman_to_integer(s):
    # create dictionary
    roman_values = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100, 'D': 500,
        'M': 1000
    }
    total = 0
    prev_value = 0

    # Reverse Traverse String

    for char in reversed(s):
        current_value = roman_values[char]

        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        prev_value = current_value

    # final ending
    return total


print(roman_to_integer("MCMQWET"))
