# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
masssiv = []
n = int(input("Введите количество элементов массива: "))

def Massiv(n):
    for i in range(n):
        masssiv.append(random.randint(1,100))
    return masssiv

print(Massiv(n))

n_min = int(input("Введите минимум диапазона: "))
n_max = int(input("Введите максимум диапазона: "))

index_n = []

def Index_Find(n_min, n_max):
    for i in range(len(masssiv)):
        if masssiv[i] >= n_min and masssiv[i] <= n_max:
            index_n.append(i)
    return index_n

print(Index_Find(n_min, n_max))
