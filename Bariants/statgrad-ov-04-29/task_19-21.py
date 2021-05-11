"""
Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежат две кучи камней.
Игроки ходят по очереди, первый ход делает Петя. За один ход игрок может добавить
в одну из куч один камень или увеличить количество камней в куче в три раза.
Например, пусть в одной куче 5 камней, а в другой 9 камней; такую позицию мы будем обозначать (5, 9).
За один ход из позиции (5, 9) можно получить любую из четырёх позиций: (6, 9), (15, 9), (5, 10), (5, 27).
Чтобы делать ходы, у каждого игрока есть неограниченное количество камней.
Игра завершается в тот момент, когда суммарное количество камней в кучах становится не менее 79.
Победителем считается игрок, сделавший последний ход, то есть первым получивший позицию,
в которой в кучах будет 79 или больше камней.
В начальный момент в первой куче было 6 камней, во второй куче – 𝑆 камней, 1≤𝑆≤72.
Будем говорить, что игрок имеет выигрышную стратегию, если он может выиграть при любых ходах противника.

Известно, что Ваня выиграл своим первым ходом после неудачного первого хода Пети.
Назовите минимальное значение 𝑆, при котором это возможно.

Найдите все такие значения 𝑆, при которых у Пети есть выигрышная стратегия,
причём Петя не может выиграть первым ходом,
но может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.
Найденные значения запишите в ответе в порядке возрастания (в отдельные поля для ответов).

Укажите максимальное значение 𝑆, при котором у Вани есть выигрышная стратегия,
позволяющая ему выиграть при любой игре Пети.

24
8 20 23
24

ВАЖНО! Для поиска ответа в 19 задаче, можно заменить all на any в условии, возвращающим V1
(только на время выполнения задания 19).
Таким образом минимальное значение камней в куче, которое  равно V1 - ответ на задание.
"""
from functools import *


def moves(h):
    a, b = h
    return (a + 1, b), (a * 3, b), (a, b + 1), (a, b * 3)


@lru_cache(None)
def game(h):
    a, b = h
    if a + b >= 79:
        return 'W'

    if any(game(m) == 'W' for m in moves(h)):
        return 'P1'
    if all(game(m) == 'P1' for m in moves(h)):
    # if any(game(m) == 'P1' for m in moves(h)):  # для 19 задания
        return 'V1'
    if any(game(m) == 'V1' for m in moves(h)):
        return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(h)):
        return 'V2'


for s in range(1, 72 + 1):
    h = 6, s
    print(s, game(h))
