"""
Задание 5 (№1424).
На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
1) Строится двоичная запись числа N.
2) Затем справа дописываются два разряда: символы 01, если число N чётное, и 10, если нечётное.
Полученная таким образом запись (в ней на два разряда больше, чем в записи исходного числа N)
является двоичной записью искомого числа R. Укажите минимальное число N,
после обработки которого автомат получает число, большее 281. В ответе это число запишите в десятичной системе.
"""
for n in range(1, 512):
    binary = bin(n)[2:]
    if n % 2 == 0:
        binary += '01'
    else:
        binary += '10'
    R = int(binary, 2)
    if R > 281:
        print(n)
        break
