# Set:
# Уникальные элементы:
# Создайте функцию, которая принимает список и возвращает множество уникальных элементов из этого списка.

# def unique_elements(input_list):
#     return set(input_list)
# my_list = [1, 2, 2, 3, 4, 5, 5]
# result_set = unique_elements(my_list)
# print(my_list)
# print(result_set)



# Объединение множеств:
# Напишите программу, которая объединяет два множества и выводит результат.


# def union_sets(set1, set2):
#     result_set = set1.union(set2)
#     return result_set

# set_a = {1, 2, 3, 4}
# set_b = {3, 4, 5, 6}

# result_union = union_sets(set_a, set_b)

# print(set_a)
# print(set_b)
# print(result_union)



# Пересечение множеств:
# Напишите функцию, которая находит и возвращает пересечение двух множеств.

# def intersection_sets(set1, set2):
#     result_set = set1.intersection(set2)
#     return result_set

# set_a = {1, 2, 3, 4}
# set_b = {3, 4, 5, 6}

# result_intersection = intersection_sets(set_a, set_b)

# print(set_a)
# print(set_b)
# print(result_intersection)



# Удаление дубликатов из списка:
# Создайте функцию, которая принимает список и возвращает новый список без повторяющихся элементов, используя множество.


# def remove_duplicates(input_list):
#     unique_set = set(input_list)
#     result_list = list(unique_set)
#     return result_list
# my_list = [1, 2, 2, 3, 4, 5, 5]
# result_without_duplicates = remove_duplicates(my_list)

# print("Исходный список:", my_list)
# print("Список без повторяющихся элементов:", result_without_duplicates)




# Проверка подмножества:
# Напишите функцию, которая проверяет, является ли одно множество подмножеством другого.

# def is_subset(set1, set2):
#     return set1.issubset(set2)
# set_a = {1, 2, 3}
# set_b = {1, 2, 3, 4, 5}
# result_is_subset = is_subset(set_a, set_b)
# print("Множество A:", set_a)
# print("Множество B:", set_b)
# print("Является ли множество A подмножеством множества B:", result_is_subset)

# frozenset

# Frozenset:
# Создание frozenset:
# Создайте frozenset из списка чисел и попробуйте изменить его 
# (вставить новый элемент), чтобы увидеть, что это неизменяемый объект.

# iman = {1, 2, 3, 4, 5}
# frozen_set = frozenset(iman)
# try:
#     frozen_set.add(6)
# except AttributeError as e:
#     print ({e})
# print(frozen_set)

# 2 
# Пересечение frozenset:
# Напишите функцию, которая находит и возвращает пересечение двух frozenset.

# def intersection_of_frozensets(set1, set2):
#     return set1 & set2
# frozen_set1 = frozenset({1, 2, 3, 4, 5})
# frozen_set2 = frozenset({3, 4, 5, 6, 7})
# result_intersection = intersection_of_frozensets(frozen_set1, frozen_set2)
# print(result_intersection)

# 3Сравнение frozenset:
# Напишите программу, которая сравнивает два frozenset и выводит результат.

# def compare_frozensets(set1, set2):
#     print("set1 == set2:", set1 == set2)
#     print("set1 != set2:", set1 != set2)
#     print("set1 < set2:", set1 < set2)
#     print("set1 <= set2:", set1 <= set2)
#     print("set1 > set2:", set1 > set2)
#     print("set1 >= set2:", set1 >= set2)
# frozen_set1 = frozenset({1, 2, 3, 4, 5})
# frozen_set2 = frozenset({3, 4, 5, 6, 7})
# compare_frozensets(frozen_set1, frozen_set2)

# 4 Преобразование frozenset в список:
# Создайте frozenset и преобразуйте его в список.
# Сложение frozenset:

# frozen_set = frozenset({1, 2, 3, 4, 5})
# list_from_frozenset = list(frozen_set)
# print(frozen_set)
# print(list_from_frozenset)
# another_frozen_set = frozenset({4, 5, 6, 7})
# result_union = frozen_set | another_frozen_set
# print(result_union)



# Lambda:
# Сортировка списка строк по длине:

# iman_list = ["apple", "banana", "kiwi", "orange", "grape"]
# sorted_list = sorted(iman_list, key=lambda x: len(x))
# print(sorted_list)

