#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Пример:
#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10

def change_to2(n):
    remainder = ''
    if n == 0:
        remainder = 0
    while n > 0:
        remainder = str(n % 2) + remainder
        n = n // 2
    return remainder
    
print(change_to2(int(input(f'Задайте число:\t'))))

