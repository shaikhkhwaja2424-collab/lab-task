def character_count(text):
    result = {}

    for char in text:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    return result

text = "khwaja"

print(character_count(text))