# 1) Создайте вручную список из 15 элементов (название городов, музыки, машины). Сделайте срез от 2-го индекса до 7-го


# list= ["Ош", "Бишкек", "Жалал-абад", "Ыссык-кол ", "баткен", "lexus", "toyota", "mercedes", "bmw", "wolksfsgen",
# "mustang", "hyunday", "ford", "samsung", "iphone", "kyrgyzstan",] 
# print(list[2:7])


# 2) Создайте вручную список из чисел и выведите их в обратном порядке


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
# print (numbers[::-1])
# print (numbers)


#3) 3) Даны два списка, удалите все элементы первого списка из второго, то есть дубликаты.


# a = [1, 3, 4, 5] 
# b = [4, 5, 6, 7]
# c = set(a+b)
# print (c)

# 4) Найдите наименьший элемент в списке из задания 2


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
# print(min(numbers))


# 5) Удалите все элементы из списка, созданного в задании 2


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
# print (numbers[::-1])
# print (numbers)
# numbers.clear ()
# print (numbers)

# 6) Найдите сумму элементов списка из задания 2


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
# print (sum(numbers))


#  7) Найдите среднее арифметическое элементов списка из задания 2


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# number = (sum(numbers) / len(numbers))
# print (number)


#  7) 8) Создайте плейлист из 10 любимых песен, поменяйте 4-й с 8-м и выведите на экран весь плейлист

# my_list = ["starboy", "reminder", "macan", "metaphorip" , "sebelep", "nazik gulim", "qazir qaydasyb" , "tun", "interword"]
# list = my_list[4], my_list[8] = my_list[8],my_list[4]
# print (list)



#  9 Есть список 

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
# 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58,
# 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215,
# 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240,
# 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265,
# 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290,
# 291, 292, 293, 294, 295, 296, 297, 298, 299, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124,
# 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
# 150, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 
# 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 
# 299, 110]
# #Выясните сколько раз цифра 110 встречается в списке
# print (numbers.count(110))



# 10) Написать программу, которая будет проверять пароль. Пусть программа в начале запросит пароль у пользователя. 
# В самой программе сохраните определенный пароль и сравните его с тем, который был введен пользователем. В случае, если
#  пароли совпадают, то выведете на экран следующее сообщение: ‘Password is correct. You are welcome’ Если нет: sword 
# is incorrect. Please, try again’

# password1 = '9996'
# password = input("введите пароль : ")
# if password == password1:
#     print("Password is correct. You are welcome")
# else:
#     print ("Please, try again")


# 11) Написать программу, которая будет спрашивать у пользователя температуру за окном. 
# Используя условные конструкции if elif else, напишите программу, которая выводит на экран следующее: 


#  При условии меньше -30 градусов: “Там так холодно, лучше дома сиди!” 
#  При условии от -30 до 0: “Холодновато. Оденься потеплее!” 
#  При условии от 0 до 15: “Прохладно. Куртку накинь!
#  При условии от 15 до 30: “Тепло. Иди погуляй в парке!”
#  При условии от 30 до 50 включительно: “Ого, как жарко!”
#  При условии выше 50: “Там такая жара, лучше сиди дома!” 
#  В других случаях: “Ошибка!

# weather = int(input("сколько градусов за окном?"))
# if weather <-30:
#     print ("там прохладно ,лучше дома сиди! ")
# elif weather >-30 and weather <=0:
#     print ("холодновато. оденься потеплее!")
# elif weather >0 and weather <15:
#     print ("прохладно. куртку накинь!")
# elif weather >15 and weather <30:
#     print ("тепло . иди погуляй в парке")
# elif weather >30 and weather <50:
#     print ("ого, как жарко!")
# else:
#     print ("там такая жара, лучше сиди дома!")







# 12)  Представьте, что вы разрабатываете программу для автоматического определения времени суток на основе текущего часа.
# Ваша задача - написать программу на Python, которая принимает на вход значение текущего часа (от 0 до 23) и выводит 
# соответствующее время суток: "Ночь (0 - 6)", "Утро (7 - 12)", "День (13 - 18)" или "Вечер (18 - 23)". Используйте 
# условные операторы (if, elif, else) для определения времени суток. Пример: Введите текущий час (от 0 до 23): 14 День

# hour = int(input(" введите текущее  время суток "))
# if 0 <= hour <=6:
#     print ("ночь")
# elif 7 <= hour <=12 :
#     print ("утро")
# elif 13 <= hour <=  18:
#     print ("день")
# elif 19 <= hour <=  23:
#     print ("ночь")
# else:
#     print ("ошибка")



# ДОП ЗАДАЧА:

# 1) Вы разрабатываете программу для оценки успеваемости студентов на основе введенной оценки. 
# Напишите программу на Python, которая будет принимать на вход оценку студента (от 0 до 100) и 
# выводить соответствующую оценку: "Отлично", "Хорошо", "Удовлетворительно", "Неудовлетворительно" или "Студент 
# должен пересдать экзамен". Используйте условные операторы (if, elif, else) для определения оценки.

#  Если оценка равен или выше 90, выведите “Отлично”
#  Если оценка между 80 и до 90, выведите “Хорошо”
#  Если оценка между 70 и до 80, выведите “Удовлетворительно”


