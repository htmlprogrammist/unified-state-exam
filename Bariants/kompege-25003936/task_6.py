"""
Задание 6 (№1425).
Найдите максимальное значение s, при котором в результате работы программы на экране будет напечатано число 32.
Для Вашего удобства программа представлена на четырех языках программирования.
"""
s = int(input())
n = 1
while s < 94:
    s += 8
    n *= 2
print('n:', n)

number = 1
while number < 1000:
    s = number
    n = 1
    while s < 94:
        s += 8
        n *= 2
    if n == 32:
        print('S:', number)
    number += 1
