# 1. Чтение файла и вывод его содержимого:
#    Создайте программу, которая открывает текстовый файл и выводит его содержимое на экран.

# iman = 'test.txt'
# with open (iman, 'r')as file:
#     zhoroeevv = file.read()
#     print(zhoroeevv)


# 2. Подсчет количества строк в файле:   
# Напишите программу, которая считает количество строк в текстовом файле и выводит это число.
#   

# iman = "test.txt"
# with open(iman, 'r') as file:
#    num_lines = sum(1 for line in file)
# print(f"Количество строк в файле {iman}: {num_lines}")   
# file_path = 'test.txt'
# num_lines(iman) 

# 3. Поиск определенного слова в файле:   
# Создайте программу, которая открывает текстовый файл и проверяет, 
# содержится ли в нем определенное слово. Если слово найдено, программа 
# должна вывести сообщение об успешном поиске.


# def iman(file_path, target_word):

#         with open(file_path, 'r') as file:
#             content = file.read()
#             if target_word in content:
#                 print("слово найдено")
#             else:
#                 print("слово не найдено ")

# file_path = 'test.txt' 
# target_word = 'iman' 
# iman(file_path, target_word)




# 4. Запись в файл:   Попросите пользователя ввести некоторый текст 
# и сохраните его в текстовом файле.

# def iman (file_path, text):
#     with open (file_path, 'w') as file:
#          file.write (text)
#          print(f"Текст успешно сохранен в файле {file_path}")
# user_text = input("Введите текст для сохранения в файле: ")
         
# file_path = 'test.txt'
# iman(file_path, user_text)


# 5. Копирование файла:
#    Напишите программу, которая копирует содержимое одного файла в другой файл.

# def copy_file(source_path, destination_path):
#     with open(source_path, 'rb') as source_file, open(destination_path, 'wb') as destination_file:
#         content = source_file.read()
#         destination_file.write(content)          
#         print(f"Файл {source_path} успешно скопирован в {destination_path}.")
# source_file_path = 'test.txt'
# destination_file_path = 'user.txt'
# copy_file(source_file_path, destination_file_path)




# 6. Подсчет количества слов в файле:
#    Создайте программу, которая подсчитывает количество слов в текстовом файле и выводит это число.


# def iman (file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#          content = file.read()
#          words = content.split()
#          print(f"количество слов в файле {file_path}: {len(words)} ")
# file_path = 'test.txt'
# iman(file_path)


# 7. Перезапись файла:
#    Напишите программу, которая открывает файл, перезаписывает его содержимое новым текстом и сохраняет изменения.

# def iman (file_path , new_content):
#     with open(file_path,'w') as file:
#       file.write(new_content)
#     print (f"содержимое файла '{file_path}' успешно перезаписано.")
# file_path = 'test.txt'
# new_content = "zhoroeevv iman . +996 777 411 000"
# iman(file_path , new_content)






