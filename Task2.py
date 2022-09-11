#Напишите программу, которая найдёт произведение пар чисел списка. 
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

print(f'Задайте список через пробел:', end=' ')
n = [str(i) for i in input().split()]
print(f'Заданный список: {n}')

def mult(list_1):
    result = []
    if len(n) % 2 == 0:
        for i in range(int(len(list_1) / 2)):
            num = int(list_1[i]) * int(list_1[-i-1])
            result.append(num)
    elif len(list_1) == 1:
            num = int(list_1[0]) ** 2
            result.append(num)  
    else:
        for i in range(len(list_1) // 2 + 1):
            num = int(list_1[i]) * int(list_1[-i-1])
            result.append(num) 
    return result                     

print(mult(n))












