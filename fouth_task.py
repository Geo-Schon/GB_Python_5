"""

Создайте функцию генератор чисел Фибоначчи

"""


def fibonacci(num):
    fn = [0, 1, ]
    for i in range(2, num):
        fn.append(fn[i - 1] + fn[i - 2])
    return fn
