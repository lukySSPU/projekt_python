from structures import charFrequency

sentence = "Tři sta třicet tři stříbrných stříkaček přestříkalo přes tři sta třicet tři stříbrných střech."

result = charFrequency(sentence)

print("Věta:", sentence)
print("Četnost výskytu písmen:")
print("-----------------------")
for char, count in result:
    print(f"('{char}', {count}),")
