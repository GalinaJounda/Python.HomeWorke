# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4

# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5

# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from random import sample

def list_rand_num(count: int) -> list:
    if count < 0:
        print("Negative number!")
        return []

    list_num = sample(range(1, count * 2), count)
    return list_num

def prod_pairs(list_num: list):
    res_list = []
    len_list = len(list_num)

    for k in range(len_list // 2):
        res_list.append(list_num[k] * list_num[len_list - k - 1])

    if len_list % 2:
        res_list.append(list_num[len_list // 2])
    return res_list

all_list = list_rand_num(int(input("Number: ")))
print(all_list)
print(prod_pairs(all_list))

