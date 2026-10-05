def longest_word(sentence):
    words = sentence.split()

    longest = words [0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest

# print(longest_word("Python is very powerful"))
print(longest_word("I am learning Software Testing at TOPS Technologies."))