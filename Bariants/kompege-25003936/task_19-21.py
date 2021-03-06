"""
Задание 19 (№1420). Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит две кучи камней.
Игроки ходят по очереди, первый ход делает Петя. За один ход игрок может добавить в одну из куч (по своему выбору)
один камень, или увеличить количество камней в куче в два раза. Например, пусть в одной куче 10 камней,
а в другой 5 камней; такую позицию в игре будем обозначать (10, 5). Тогда за один ход можно получить любую из четырёх
позиций: (11, 5), (20, 5), (10, 6), (10, 10). Для того чтобы делать ходы, у каждого игрока есть неограниченное
количество камней.
Игра завершается в тот момент, когда произведение количеств камней в кучах становится не менее 63.
Победителем считается игрок, сделавший последний ход, т.е. первым получивший такую позицию,
при которой произведение числа камней в кучах будет 63 или более.
В начальный момент в первой куче было 2 камня, во второй куче - S камней; 1 ≤ S ≤ 31.
Будем говорить, что игрок имеет выигрышную стратегию, если он может выиграть при любых ходах противника.
Описать стратегию игрока – значит описать, какой ход он должен сделать в любой ситуации, которая ему может
встретиться при различной игре противника. В описание выигрышной стратегии не следует включать ходы играющего
по этой стратегии игрока, не являющиеся для него безусловно выигрышными, т.е. не являющиеся выигрышными независимо
от игры противника.

Найдите значение S, при которых Петя не может выиграть за один ход, но при любом ходе Пети Ваня может выиграть
своим первым ходом?

Задание 20 .
Для игры, описанной в предыдущем задании, найдите минимальное и максимальное значение S,
при котором у Пети есть выигрышная стратегия, причём одновременно выполняются два условия:
- Петя не может выиграть за один ход;
- Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.

Задание 21 .
Для игры, описанной в задании 19, найдите наибольшее значение S, при котором одновременно выполняются два условия:
– у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Пети;
– у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.

15
7 14
13
"""
from functools import lru_cache


def moves(h):
    a, b = h
    return (a + 1, b), (a * 2, b), (a, b + 1), (a, b * 2)


@lru_cache(None)
def game(h):
    a, b = h
    if a * b >= 63:
        return 'W'

    if any(game(m) == 'W' for m in moves(h)):
        return 'P1'
    if all(game(m) == 'P1' for m in moves(h)):
        return 'V1'
    if any(game(m) == 'V1' for m in moves(h)):
        return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(h)):
        return 'V2'


for s in range(1, 31 + 1):
    h = 2, s
    if game(h) == 'V1':
        print(s, game(h))
    if game(h) == 'P2':
        print(s, game(h))
    if game(h) == 'V2':
        print(s, game(h))
