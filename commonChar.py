def commmon_characters(text1, text2):
    result = ""

    for char in text1:
        if char in text2 and char not in result:
            result += char

    return result

# print(commmon_characters("apple", "plane"))
print(commmon_characters("Ahmedabad", "Hydrabad"))