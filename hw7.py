# def correct_sentence(text):
#     text = text[0].upper() + text[1:]
#
#     if not text.endswith("."):
#         text = text + "."
#
#     return text
#
#
# assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
# assert correct_sentence("hello") == "Hello.", 'Test2'
# assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
# assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
# assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
#
# print('ОК')

# def second_index(text, some_str):
#     first = text.find(some_str)
#
#     second = text.find(some_str, first + len(some_str))
#
#     if second == -1:
#         return None
#
#     return second
#
#
# assert second_index("sims", "s") == 3, 'Test1'
# assert second_index("find the river", "e") == 12, 'Test2'
# assert second_index("hi", "h") is None, 'Test3'
# assert second_index("Hello, hello", "lo") == 10, 'Test4'
#
# print('ОК')


# def common_elements():
#     list_3 = [x for x in range(100) if x % 3 == 0]
#     list_5 = [x for x in range(100) if x % 5 == 0]
#
#     set_3 = set(list_3)
#     set_5 = set(list_5)
#
#     return set_3 & set_5
#
#
# assert common_elements() == {0, 75, 45, 15, 90, 60, 30}


