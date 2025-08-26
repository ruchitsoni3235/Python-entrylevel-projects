def compressed_str(s):
    compressed_result = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed_result.append(s[i - 1] + str(count))
            count = 1

    # 👇 ये lines अब loop के बाहर हैं
    compressed_result.append(s[-1] + str(count))
    compressed_string = ''.join(compressed_result)

    if len(compressed_string) < len(s):
        return compressed_string
    else:
        return s


print(compressed_str("aaabbcc"))  # ✅ अब देगा a3b2c2

