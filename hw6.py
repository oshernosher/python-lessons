# import string
#
# letters = input()
#
# print("Ты ввел:", letters)
#
# start, end = letters.split("-")
#
# start_index = string.ascii_letters.index(start)
# end_index = string.ascii_letters.index(end)
#
# print(string.ascii_letters[start_index:end_index + 1])


# seconds = int(input())
#
# days = seconds // 86400
# seconds = seconds % 86400
#
# hours = seconds // 3600
# seconds = seconds % 3600
#
# minutes = seconds // 60
# seconds = seconds % 60
#
#
# time = (
#     str(hours).zfill(2)
#     + ":"
#     + str(minutes).zfill(2)
#     + ":"
#     + str(seconds).zfill(2)
# )
#
#
# if days % 10 == 1:
#     day_word = "день"
#
# elif 2 <= days % 10 <= 4:
#     day_word = "дня"
#
# else:
#     day_word = "дней"
#
#
# print(f"{days} {day_word}, {time}")


# number = int(input())
#
# while number > 9:
# 
#     product = 1
#
#     while number > 0:
#         digit = number % 10
#         product *= digit
#         number = number // 10
#
#     number = product
#
# print(number)


