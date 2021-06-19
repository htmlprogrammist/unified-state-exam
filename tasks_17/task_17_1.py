"""
Назовём натуральное число подходящим, если ровно два из его делителей
входят в список (11, 13, 17, 19). Определите количество подходящих чисел,
принадлежащих отрезку [11 000; 22 000], а также наименьшее из таких чисел.
В ответе запишите два целых числа: сначала количество, затем наименьшее
число.
"""

dividers = []
k = 0
n = 0
# for i in range(11000, 22000 + 1):
#     k = 0
#     if i % 11 == 0:
#         k += 1
#     if i % 13 == 0:
#         k += 1
#     if i % 17 == 0:
#         k += 1
#     if i % 19 == 0:
#         k += 1
#     if k == 2:
#         n += 1
#         dividers.append(i)
# print(n, min(dividers))

min_i = 0
for i in range(22000, 11000 - 1, -1):
    k = 0
    if i % 11 == 0:
        k += 1
    if i % 13 == 0:
        k += 1
    if i % 17 == 0:
        k += 1
    if i % 19 == 0:
        k += 1
    if k == 2:
        min_i = i
        n += 1
print(n, min_i)
