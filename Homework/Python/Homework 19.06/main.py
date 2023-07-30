# numbers = [12, 34, 1, 9, 65, 22]
# j = len(numbers)
# temp = 0

# for num in range(j-1):
#     for i in range(j-1):
#         if numbers[i] > numbers[i+1]:
#             temp = numbers[i]
#             numbers[i] = numbers[i+1]
#             numbers[i+1] = temp

# print(numbers)


# list = ['John', 'Sara', 'Bill', 'William', 'Sara', 'Bill']
# new_list = []

# new_list = set(list)

# print(new_list)


numbers = [12, 34, 1, 10, 65, 22]

for i in numbers:
    if i % 2 != 0:
        print(f"First odd number: {i}")
        break
