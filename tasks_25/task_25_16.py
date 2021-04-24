"""
№ 1078
Пусть S - сумма натуральных чётных делителей целого числа, не считая самого числа.
Если таких делителей у числа нет, то считаем значение S равным нулю.
Напишите программу, которая перебирает целые числа из отрезка [1204300; 1204380]
в порядке возрастания и ищет среди них такие,
для которых значение S не равно нулю и кратно 10.
Программа должна найти и вывести такие числа и соответствующие им значения S.
Формат вывода:
для каждого из найденных чисел в отдельной строке сначала выводится само число,
затем значение S. Строки выводятся в порядке возрастания найденных чисел.

1204328 948760
1204354 27530
1204356 1204380
1204360 1324880
1204366 4850
1204370 291070
1204378 172070
"""
for i in range(1204300, 1204380 + 1):
    s = 0
    for j in range(2, i // 2 + 1):
        if i % j == 0 and j % 2 == 0:
            s += j
    if s != 0 and s % 10 == 0:
        print(i, s)

# for i in range(1204300, 1204380 + 1):
#     s = 0
#     for j in range(2, round(i ** 0.5) + 1):
#         if i % j == 0 and j % 2 == 0:
#             s += j
#             if (i // j) % 2 == 0:
#                 s += i // j
#         if (i ** 0.5).is_integer():
#             s += i ** 0.5
#     if s != 0 and s % 10 == 0:
#         print(i, s)
