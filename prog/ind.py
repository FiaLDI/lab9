#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# С использованием многопоточности для заданного значения x
# найти сумму ряда S с точностью члена ряда по
# абсолютному значению E = 10e-7 и произвести сравнение
# полученной суммы с контрольным значением функции
# для двух бесконечных рядов.

import math
from threading import Thread

E = 10e-7


# 1 Вариант
def calculate_row_1(target, x):
    def calculate_nextpart(results, x, cur):
        return results[-1] * x * math.log(3) / cur

    def control_value(x):
        return 3**x

    i = 0

    local_result = [1]
    while local_result[i] > E:
        local_result.append(calculate_nextpart(local_result, x, i + 1))
        i += 1
    
    target["sum_row_1"] = sum(local_result)


# 2 Вариант
def calculate_row_2(target, x):
    def calculate_nextpart(results, x):
        return results[-1] * x

    def control_value(x):
        return round(1 / (1 - x), 4)

    i = 0
    local_result = [1]
    while local_result[i] > E:
        local_result.append(calculate_nextpart(local_result, x))
        i += 1
    
    target["sum_row_2"] = sum(local_result)


def main():
    part_of_rows = {"sum_row_1": 0, "sum_row_2": 0}

    th1 = Thread(target=calculate_row_1, args=(part_of_rows, 1))
    th2 = Thread(target=calculate_row_2, args=(part_of_rows, 0.7))

    th1.start()
    th2.start()

    th1.join()
    th2.join()

    print(f"Результат {part_of_rows}")


if __name__ == "__main__":
    main()

