# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22

from random import sample

def list_rand_num(count: int) -> list:
    if count < 0:
        print("Negative number!")
       
        return []

    list_num = sample(range(1, count * 2), count)
    print(list_num)
    return list_num


def sum_add_pos(list_num: list):
    sum_num = 0
    for k in range(0, len(list_num), 2):
        sum_num += list_num[k]
    return sum_num

all_list = list_rand_num(int(input("Number: ")))
print(sum_add_pos(all_list))

