# def square_dictionary(n):
#     result = {}

#     for number in range(1, n + 1):
#         result[number] = number ** 2

#     return result

# n = 20
# print(square_dictionary(n))


def square_numbers(numbers):
    result = []

    for number in numbers:
        result.append(number ** 2)

    return result

print(square_numbers([11, 13, 17, 22, 25]))