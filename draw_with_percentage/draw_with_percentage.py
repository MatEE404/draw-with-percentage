# -*- coding: utf-8 -*-

from random import randint
from decimal import Decimal


def draw_with_percentage(percentages: list):
    """Randomize an element according to the given percentages

    :param percentages: This is a list that will contain all items with the percentage indicated.
    :return: Return the drawn element according to the set percentages.
    """

    if not len(percentages) > 0:
        raise ValueError("No item was specified")

    sum_percentages = 0
    for index, item in enumerate(percentages):
        if isinstance(item[0], str) and isinstance(item[1], str):
            item[1] = Decimal(item[1])
            sum_percentages += item[1]
        else:
            raise ValueError("Bad given items")

        if index == 0:
            item[1] = [Decimal(0), item[1]]
        else:
            start = percentages[index - 1][1][1] + Decimal("0.001") \
                if percentages[index - 1][1][1] != 0 else Decimal("0")
            end = percentages[index - 1][1][1] + item[1]
            item[1] = [start, end]

    if sum_percentages != 100:
        raise ValueError("The sum of all the percentages is not 100")

    random_number = randint(0, 100000) / 1000

    for item in percentages:
        if item[1][0] <= random_number <= item[1][1]:
            return item[0]

