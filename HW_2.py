# Task 1
# Вывести на экран циклом пять строк из нулей длиной 4, причем каждая строка должна быть пронумерована.
# Пример:
#     0 0000
#     1 0000
#     2 0000
#     3 0000
# # ....
print('Задача 1.')
for i in range(0,5):
    print(i, '0000')

# Задача 2
# Пользователь в цикле вводит 10 производных цифр. Выведите количество введеных пользователем цифр 5.
five_number = 0
for i in range(0,10):
    number_in  = int(input('введите число '))
    if number_in == 5:
        five_number += 1
print('Задача 2. Количество введеных пользователей цифра 5: ', five_number)

# Задача 3
# Вывести сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.

summ_100 = 0
for i in range(1,100):
    summ_100 += i
print('Задача 3. Сумма ряда: ', summ_100)

# Задача 4
# Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран(можно поискать в интернете алгоритм факториала в python).
def fac(n):
    if n == 0:
        return 1
    return fac(n - 1) * n

print('Задача 4. Факториал ряда чисел от 1 до 10:', fac(10))

# (!!!Подсказка на следующую задачу - превратите число в строку, а потом работайте с строкой)
# Задача 5
# Вывести цифры числа на каждой новой строке.
number_str  = input('введите число ')
for i in number_str:
    print(i)