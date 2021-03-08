"""
№ 438, Джобс 05.10.2020
Исполнитель Джысум преобразует число, записанное на экране.
У исполнителя есть три команды, которым присвоены номера:
1. Прибавить значение младшего разряда
2. Умножить на значение старшего разряда
3. Прибавить разность большего и меньшего по значению разрядов
Первая команда не применима к числам, кратным 10.
Вторая команда не применима к числам, меньшим 20.
Например, при применении команды 1 к числу 19 получим число 28,
при применении команды 2 к числу 22 – 44, команды 3 к 41 – 44.
Сколько существует таких программ, которые исходное число 21
преобразуют в число 62?

142
"""
k = [0] * (62 + 1)
k[21] = 1
for n in range(21, 62 + 1):
    senior = n // 10
    junior = n % 10
    if n % 10 != 0 and n + junior <= 62:
        k[n + junior] += k[n]

    if n > 20 and n * senior <= 62:
        k[n * senior] += k[n]

    if n + abs(senior - junior) <= 62:
        k[n + abs(senior - junior)] += k[n]

print(k[62])
