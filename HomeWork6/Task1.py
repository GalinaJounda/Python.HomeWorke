# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
# in      9
# out     [15, 16, 2, 3, 1, 7, 5, 4, 10]
#         [16, 3, 7, 10]

# in     10
# out    [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
#        [24, 15, 23, 25]

from random import sample


def random_list(num):
    return [i for i in sample(range(1, 20), num)]


def exit_list(export_list):
    return [export_list[i] for i in range(1, len(export_list)) if export_list[i] > export_list[i-1]]


one_list = random_list(int(input("Введите длину списка: ")))
print(one_list)
print(exit_list(one_list))