"""
В текстовом файле записан набор пар натуральных чисел, не превышающих 10 000.
Необходимо выбрать из набора некоторые пары так, чтобы первое число в каждой выбранной паре было нечётным,
сумма бо́льших чисел во всех выбранных парах была нечётной, а сумма меньших – чётной.
Какую наибольшую сумму чисел во всех выбранных парах можно при этом получить?

Входные данные
Первая строка входного файла содержит целое число 𝑁 – общее количество чисел в наборе.
Каждая из следующих 𝑁 строк содержит одно число.

Пример входного файла
4
5 2
8 15
7 14
11 9
В данном случае есть три подходящие пары: (5, 2), (7, 14) и (11, 9).
Пара (8, 15) не подходит, так как в ней первое число чётное. Чтобы удовлетворить требования,
надо взять пары (7, 14) и (11, 9). Сумма бо́льших чисел в этом случае равна 25, сумма меньших равна 16.
Общая сумма равна 41. В ответе надо указать число 41.

Вам даны два входных файла (A и B), каждый из которых имеет описанную выше структуру.
В ответе укажите два числа: сначала значение искомой суммы для файла A, затем для файла B.

44067 301653067
"""
f = open('sg_2020-2021_inf5_27/25-A.txt')
n = int(f.readline())

