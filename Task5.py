#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#Пример:
#- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]  

n = int(input('Введите число k:\t'))

result1 = []
result2 = []

def fib_pl(n): 
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1  
    else: 
        return fib_pl(n-1) + fib_pl(n-2)

def fib_otr(n): 
    if n == 1:
        return 1
    elif n == 2:
        return -1  
    else: 
        return ((-1) ** (n + 1)) * fib_pl(n) 
 
for i in range (n+1):
    result1.append(fib_pl(i))
for i in range(1, n+1):
    result2.append(fib_otr(i))

result2 = result2[::-1]    
print(result2 + result1)    
    
