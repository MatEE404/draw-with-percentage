""" Draw with Percentage """

from random import randint


def draw_with_percentage(percentages: list):
    """

    :param percentages:
    :return:
    """

    if not len(percentages) > 0:
        raise Exception("No item was specified")

    sum_percentages = 0
    for index, item in enumerate(percentages):
        if isinstance(item[0], str) and isinstance(item[1], float) or isinstance(item[1], int):
            sum_percentages += item[1]
        else:
            raise Exception("Bad given items")

        if index == 0:
            item[1] = [0, item[1]]
        else:
            start = percentages[index - 1][1][1] + 0.001 if percentages[index - 1][1][1] != 0 else 0
            end = percentages[index - 1][1][1] + item[1]
            item[1] = [start, end]

    if sum_percentages != 100:
        raise Exception("The sum of all the percentages is not 100")

    random_number = randint(1000, 100000) / 1000

    for item in percentages:
        if item[1][0] <= random_number <= item[1][1]:
            return item[0]


if __name__ == "__main__":
    obj = [
        ["milk", 24.5],
        ["apple", 24.91],
        ["bread", 39.09],
        ["banana", 11.5]
    ]

    print(draw_with_percentage(obj))
