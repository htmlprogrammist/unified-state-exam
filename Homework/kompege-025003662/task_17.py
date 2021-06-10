"""
Задание 17 (№1372).
Рассматривается множество целых чисел, принадлежащих числовому отрезку [25552; 58885],
которые имеют не менее 15 двузначных делителей.
Найдите наибольшее из таких чисел и их количество.
В ответе укажите два числа – сначала количество найденных чисел, затем наибольшее найденное число.
"""
counter = 0
mx = 0

for i in range(25552, 58885 + 1):
    d = set()
    for j in range(10, int(i ** 0.5) + 1):
        if i % j == 0:
            if len(str(j)) == 2:
                d.add(j)
            if len(str(i // j)) == 2:
                d.add(j)
    if len(d) >= 15:
        counter += 1
        mx = i
print(counter, mx)
