# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
from pathlib import Path
import re
path = Path.cwd() / 'test_file' / 'task_3.txt'
path_new = Path.cwd() / 'test_file' / 'task1_answer.txt'
with open(path, "r", encoding='utf-8') as f:
    purchases = f.read().strip().split('\n\n')
    prices = []
    for purchase in purchases:
        prices.append(sum(map(int, purchase.strip().split('\n'))))
    prices.sort(reverse=True)
    three_most_expensive_purchases = sum(prices[:3])

assert three_most_expensive_purchases == 202346
