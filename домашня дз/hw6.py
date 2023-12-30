#1   # Напишите функцию -- чат-бот с бесконечным циклом, который
# a. Всегда отвечает “Конечно!” на любой вопрос
# b. Всегда отвечает “Успокойся”, если ты кричишь на него ВОТ ТАК!
# c. Всегда отвечает “Как классно, когда ты молчишь. Продолжай в том же
# духе!” Если вызвал функцию, но ничего не передал.
# d. В любых других случаях, отвечает “ну и что”

# def user(): 
#     while True:
#         user = input("Можете задать вопрос: ")
#         if "?" in user:
#             print("Конечно!")
#         elif "!" in user:
#             print("Успокойся")
#         elif "" in user:
#             print("Как классно, когда ты молчишь. Продолжай в том же духе!")
#         else:
#             print("ну и что")
# user()
    




#2   # Напишите функцию, которая принимает фразу, и возвращает его сокращенную
# форму.
# Например: Кыргызская Республика -- КР. Ruby on Rails -- ROR. For your interest --
# FYI и т.п.

# def Iman():
#     user = input("Введите фразу: ")
#     user1 = user.split()
#     a = []
#     for word in user1:
#         a.append(word[0].upper())
#     b = "".join(a)
#     print(b)
# Iman()



#3    # Напишите функцию, которая проверяет, сколько раз каждое слово в переданной
# фразе было использовано. Например: “Money, money, money, it’s always sunny, in
# the richmen’s world”. money: 3, it’s: 1, always: 1, sunny: 1, in: 1, the: 1, richmen’s: 1,
# world: 1.

# def Iman():
#     iman = "Money, money, money, it's always sunny, in the richmen's world".lower()
#     print("money:", iman.count("money"))
#     print("it's:", iman.count("it's"))
#     print("always:", iman.count("always"))
#     print("sunny:", iman.count("sunny"))
#     print("in:", iman.count("in"))
#     print("the:", iman.count("the"))
#     print("richmen's:", iman.count("richmen's"))
#     print("world:", iman.count("world"))
# Iman()






#4    # Напишите функцию, которая принимает слово и возвращает True, если слово
# изограмма (т.е. все буквы в слове уникальны). Иначе возвращает False.

# def isogram(word):
#     word = word.lower()
#     unique_letters = set()
#     for letter in word:
#         if letter in unique_letters:
#             return False
#         unique_letters.add(letter)
#     return True
# word1 = "Hello"
# word2 = "Привет"
# print(isogram(word1))
# print(isogram(word2))



#5 Напишите функцию где мы передаем через аргументы число n, надо вывести сумму чисел n и“перевёрнутого” n, 
#например: n = 27, тогда перевёрнутое n это 72
# def im():
#     n = int(input("Введите число: "))
#     reverse = int(str(n)[::-1])
#     print("Сумма чисел", n, "и", reverse, "равна",)
# im()
