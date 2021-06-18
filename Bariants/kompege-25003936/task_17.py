"""
Задание 17 (№1407).
Рассматривается множество целых чисел, принадлежащих числовому полуинтервалу [1206; 14993),
которые оканчиваются либо на 3, либо на 6 и не делятся на 3, 4, 5.
Найдите количество таких чисел и минимальное из них.
В ответе запишите два целых числа: сначала количество, затем минимальное число.
Для выполнения этого задания можно написать программу или воспользоваться редактором электронных таблиц.
"""
counter = 0
m = 99999999999

for i in range(1206, 14993):
    if (i % 10 == 3 or i % 10 == 6) and i % 3 != 0 and i % 4 != 0 and i % 5 != 0:
        counter += 1
        m = min(m, i)

print(counter, m)
