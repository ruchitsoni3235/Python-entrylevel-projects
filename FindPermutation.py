def find_permutation(s):
    #base case
    if len(s) == 1:
        return [s]

    # step 2- Loop Style Character
    permutations = []
    for i in range(len(s)):
        current_character = s[i]

        # step 3 slicing
        remaining_char = s[:i] + s[i + 1:]

        #step 4 Recursion

        remaining_permutations = find_permutation(remaining_char)

        # step 5 Join method
        for p in remaining_permutations:
            permutations.append(current_character + p)
            # step 6 Return Result
    return permutations


print(find_permutation("abc"))
