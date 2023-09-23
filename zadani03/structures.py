def charFrequency(sentence):
    char_count = {}

    for char in sentence:
        if char != ' ':
            char_count[char] = char_count.get(char, 0) + 1

    sorted_char_count = sorted(char_count.items(), key=lambda x: x[1], reverse=True)

    return sorted_char_count