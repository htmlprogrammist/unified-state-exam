"""
№ 68, Джобс 31.08.2020
Задача робота заполнить как можно большее количество ящиков монетами в количестве 100 штук.
Роботу по конвейеру поступают корзины с монетами. В каждой корзине может быть от 1 до 99 монет.
Известно, что робот может высыпать в каждый ящик один раз содержимое не более двух корзин.
Необходимо написать программу, которая определяет, сколько ящиков можно заполнить ровно 100 монетами.
Входные данные представлены в файле следующим образом.
В первой строке записано число 1 < N < 10000 – количество корзин,
в каждой из последующих N строк целое число 0 < K < 100 – количество монет в каждой корзине.
В качестве ответа дать одно число – количество ящиков, заполненных 100 монетами.

Пример организации исходных данных во входном файле:
7
10
44
66
90
65
47
34
При таких исходных данных можно заполнить только 2 ящика по 100 монет 10 + 90 и 66 + 34.

3845
"""
file = open("task_26_2.txt")
n = int(file.readline())
c = [0] * 100
for i in range(n):
    c[int(file.readline())] += 1

k = c[50] // 2

for x in range(1, 50):
    k += min(c[x], c[100 - x])

print(k)
