# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

@pytest.mark.smoke
def test_numbers_1():
    assert all_division(1, 2) == 0.5

@pytest.mark.smoke
def test_numbers_2():
    assert all_division(1, 2, 3) == 0.16666666666666666


def test_numbers_3():
    assert all_division(-2, 6) == -0.3333333333333333


def test_other_1():
    try:
        all_division('a', 'b')
    except TypeError:
        print(' Аргумент должен быть числом')


def test_zero_1():
    try:
        all_division(2, 0)
    except ZeroDivisionError:
        print(' На ноль делить нельзя')
