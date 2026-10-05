# def divisiable_by_3(numbers):
#     result = []

#     for number in numbers:
#         if number % 3 == 0:
#             result.append(number)

#     return result

# print(divisiable_by_3([16, 25, 33, 63, 52, 41, 87, 89, 59, 75, 85, 15, 95, 99]))

def divisible_by_2_and_3(numbers):
    result = []

    for number in numbers:
        if number % 2 == 0 and number % 3 == 0:
            result.append(number)

    return result

# print(divisible_by_2_and_3([6, 8, 12, 15, 18]))
print(divisible_by_2_and_3([16, 18, 32, 45, 58, 66, 72, 85, 89, 92, 96]))