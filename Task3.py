#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#Пример:
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

lists = []

def calculation (str):
    for i in range(0, len(str.split(' '))):
        number_float = float(str.split(' ')[i])
        number_int = int(number_float)
        number = round(abs(number_float - number_int), 3)
        if number == 0:
            continue
        lists.append(number)
    return lists

calculation(input(f'Задайте список чисел (дроб.часть отделяется точкой) через пробел:\t'))

print(f'Максимальное значение дробной части элемента: {max(lists)}')
print(f'Минимальное значение дробной части элемента: {min(lists)}')
result = round((max(lists) - min(lists)), 3)
print(f'Разница составляет: {result}')
