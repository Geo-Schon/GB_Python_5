"""

Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида “10.25%”. В результате получаем словарь с именем в качестве ключа и суммой премии
в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии

"""


def word_gen(names: list[str], rates: list[int], reward: list[str]) -> dict[str:float]:
    return {name: money / 100 * percent
            for name, money, percent in zip(names, rates, (float(i[:-1]) for i in reward))}
