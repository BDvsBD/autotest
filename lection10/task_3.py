# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('a, b, result', [
    pytest.param(1, 2, 0.5, marks=pytest.mark.skip('Ждем исправлений')),
    pytest.param(0.5, 3, 0.16666666666666666, marks=pytest.mark.smoke('Смоки')),
    pytest.param(-2, 6, -0.3333333333333333),
    pytest.param('a', 'b', 0), (2, 0, 0)])
def test(a, b, result):
    assert all_division(a, b) == result



