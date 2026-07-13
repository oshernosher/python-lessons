# numbers = [0, 1, 0, 12, 3]
#
# result = []
#
# for num in numbers:
#     if num != 0:
#         result.append(num)
#
# for i in range(numbers.count(0)):
#     result.append(0)
#
# print(result)

#
# numbers = [0, 1, 7, 2, 4, 8]
#
# if len(numbers) == 0:
#     result = 0
# else:
#     sum_even = 0
#
#     for i in range(len(numbers)):
#         if i % 2 == 0:
#             sum_even += numbers[i]
#
#     result = sum_even * numbers[-1]
#
# print(result)


#
# import random
# size = random.randint(3, 10)
# numbers = []
#
# for i in range(size):
#     numbers.append(random.randint(1, 10))
# print(numbers)
#
# result = [numbers[0], numbers[2], numbers[-2]]
#
# print(result)