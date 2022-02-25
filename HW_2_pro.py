# Задача 6
# Найти сумму цифр числа.
number_str  = input('введите число ')
sum_number = 0
for i in number_str:
    sum_number += int(i)
print('Задача 6. Сумма цифр числа: ', sum_number)

# Задача 7
# Найти произведение цифр числа.
number_str  = input('введите число ')
sum_number = 0
for i in number_str:
    sum_number *= int(i)
print('Задача 7. Произведение цифр числа: ', sum_number)

# Задача 8
# Пользователь должен ввести число. Ваш код должен дать ответ на вопрос: есть ли среди цифр числа 5?
# Если есть, код должен вывексти "Цифра 5 есть в числе", в противном случае вывести: "Цифры 5 нет в числе".
number_str  = input('введите число ')
for i in number_str:
    if int(i) == 5:
        ii = 1
if ii == 1:
    print('Задача 8. Цифра 5 есть в числе')
else:
    print('Задача 8. Цифры 5 нет в числе')

# Задача 9
# Найти максимальную цифру в числе
number_str  = input('введите число ')
int_val = [int(x) for x in list(set(number_str))]
print('Задача 9. Максимальная цифра: ', max(int_val))

# Задача 10
# Найти количество цифр 5 в числе
import pandas as pd
number_str  = input('введите число ')
stat = pd.DataFrame(data = set(number_str)).value_counts()
if stat[stat.index == ('5',)].empty:
    print('Задача 10. нет цифры 5')
else:
    print('Задача 10. количество петерок в числе: {}'.format(stat[stat.index == ('5',)].values[0]))