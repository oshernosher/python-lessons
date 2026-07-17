#
# import string
# import keyword
#
# name = input()
# #
# # valid = True
# #
# # # 1. Не может начинаться с цифры (заметки делаю для себя)
# # if name[0].isdigit():
# #     valid = False
# #
# # # 2. Не может содержать большие буквы
# # for i in range(len(name)):
# #     if name[i].isupper():
# #         valid = False
# #
# # # 3. Не может содержать пробелы
# # for i in range(len(name)):
# #     if name[i].isspace():
# #         valid = False
# #
# # # 4. Не может содержать знаки пунктуации (кроме "_")
# # for i in range(len(name)):
# #     if name[i] in string.punctuation and name[i] != "_":
# #         valid = False
# #
# # # 5. Не может быть ключевым словом Python
# # if name in keyword.kwlist:
# #     valid = False
# #
# # # 6. Не может содержать "__"
# # if "__" in name:
# #     valid = False
# #
# # print(valid)
#
#
#
# # while True:
# #     first_number = float(input("Enter first number: "))
# #     operation = input("Enter operation (+, -, *, /): ")
# #     second_number = float(input("Enter second number: "))
# #
# #     if operation == "+":
# #         print("Result:", first_number + second_number)
# #
# #     elif operation == "-":
# #         print("Result:", first_number - second_number)
# #
# #     elif operation == "*":
# #         print("Result:", first_number * second_number)
# #
# #     elif operation == "/":
# #         if second_number == 0:
# #             print("You cannot divide by zero!")
# #         else:
# #             print("Result:", first_number / second_number)
# #
# #     else:
# #         print("Unknown operation!")
# #
# #     answer = input("Continue? (y/n): ")
# #
# #     if answer != "y":
# #         break
# #
# # print("Calculator has stopped.")
#
#
#
#
# import string
#
# text = input("Enter text: ")
#
# # убираем все знаки пунктуации (для себя)
# for symbol in string.punctuation:
#     text = text.replace(symbol, "")
#
# # разделяем строку на слова
# words = text.split()
#
# # делаем каждое слово с большой буквы
# hashtag = ""
#
# for word in words:
#     hashtag += word.capitalize()
#
# # добавляем #
# hashtag = "#" + hashtag
#
# # ограничение 140 символов
# if len(hashtag) > 140:
#     hashtag = hashtag[:140]
#
# print(hashtag)
#
#
#
