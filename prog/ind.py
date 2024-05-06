#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import threading

E = 10e-7


def main():
    results = [1]
    x = 4

    def calculate_sum(x):
        return 3**x

    def calculate_part(results, index, x, cur):
        results[index] = 1

        def my_log():
            results[index] *= math.pow(math.log(3), cur)

        def my_pow():
            results[index] *= x**cur

        def my_fact():
            results[index] /= math.factorial(cur)

        th1 = threading.Thread(target=my_log)
        th2 = threading.Thread(target=my_pow)
        th3 = threading.Thread(target=my_fact)

        th1.start()
        th2.start()
        th3.start()

    i = 0
    while results[i] > E:
        results.append(0)
        calculate_part(results, i + 1, x, i + 1)
        i += 1
    print(f'x = {x}')
    print(round(sum(results), 5))
    print(round(sum(results), 5) == calculate_sum(x))


if __name__ == "__main__":
    main()
