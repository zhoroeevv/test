file_whrite = open ('about.txt', 'w')
file_whrite.write(("всем приветб меня зовут, иман и это прохождение в майнкрафт!"))
file_whrite.close()
                   
# file_whrite = open ('test.txt', 'w')
# file_whrite.write(("это тестовая работа"))
# file_whrite.close()

while True:
    for i in range (0,50):
        hacking = open (f'haha{i}.txt', 'w')
        hacking.write("вас взломали")
        hacking.close()

name = input("введите имя : ")
age = input("введите возрасть")
phone = input("введите номер")
file_writ = open('user.txt', 'w')
file_writ.write(f"""username:{name} age:{age} phone number:{phone}""")
file_writ.close()


#  ВТОРОЙ ВАРИАНТ!!!!


# file_read = open('user.txt', 'r')
# result = file_read.read()
# print(result)

with open ('test.txt', 'w') as write_list:
    write_list.write("привет мир!!")

with open('test.py', 'w') as write:
    num1 = int(input("введите число: "))
    num2 = int(input("введите число: "))
    n = input("выберите вариант: 1- умножение, 2- сложение, 3 - вычитание, 4- деление: ")
    
    write.write(f"num1 = {num1}\n")
    write.write(f"num2 = {num2}\n")
    write.write(f'n = \"{n}\"\n')

if n == "1":
    print(f"результат: {num1 * num2}")
elif n == "2":
    print(f"результат: {num1 + num2}")
elif n == "3":
    print(f"результат: {num1 - num2}")
elif n == "4":
    print(f"результат: {num1 / num2}")
else:
    print("такого варианта нет")



# with open  ('lesson6.py', 'r') as read_file:
#     result =read_file.read()
#     print(result)
     
    # import lesson7
    # from lesson6 import multi , dele , mines
    # from lesson6 import*
    # import random
