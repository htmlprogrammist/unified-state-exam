"""
Задание 26 (№936).
Для перевозки партии грузов различной массы выкупают место у компании перевозчиков.
Компания перевозчик не может принять на борт больше S тонн груза.
Известно, что отдельный груз нельзя разделить для перевозки,
то есть один груз должен доставляться одним рейсом на одном грузовом судне.
Так же преследуют тактику – перевезти рейсом грузы как можно большей массы.
За какое минимальное количество рейсов можно перевезти все грузы?
Входные данные представлены в файле следующим образом.
В первой строке входного файла записаны два целых числа:
N – общее количество грузов и
S – грузоподъёмность грузового судна в тоннах.
Каждая из следующих N строк содержит одно целое число < S – массу груза в тоннах.
В ответе запишите два числа – минимальное количество рейсов и суммарную массу грузов,
которые будут перевезены последним рейсом.
Пример организации исходных данных во входном файле:
6 500
140
150
160
200
220
240
При таких входных данных ответ будет 3 и 150.
Первым рейсом будет отправлено 2 груза – 240 и 220, вторым – 200, 160 и 140, третьим – 150.

423 501
"""
f = open('txt/task_26_10_example.txt')
a = f.readlines()
n = int(a[0].split()[0])
s = int(a[0].split()[1])
del a[0]
a = list(map(int, a))
a.sort(reverse=True)
current_sum = 0
counter = 0

tonns = []
for i in range(n):
    if current_sum + a[i] <= s:
        current_sum += a[i]
        counter += 1
        # print(current_sum)
        tonns.append(a[i])
        a[i] = 0
        print(tonns)
    else:
        current_sum = 0  # разгружаюсь
        tonns = []
print(counter)
