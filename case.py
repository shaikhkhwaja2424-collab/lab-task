def change_case(text):
    if len(text) > 5:
        return text.upper()
    else:
        return text.lower()


text = input("Enter a string : ")

print(change_case(text))