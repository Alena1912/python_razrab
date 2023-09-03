#Пользователь вводит натуральное k. 
# Надо сформировать многочлен такой степени, 
# где все коэффициенты случайные от -10 до 10. 

import random

k = int(input("Введите степень многочлена: "))

m = dict()

for i in range(k, -1, -1):
    m[i] = random.randint(-10,11)
    if i == 0:
        print(f' {m[i]}', end = "")
    elif m[i] == 0:
        print(end = "")
    else:
        if i == k and m[i] > 0:
            print(f' {m[i]}x^{i}', end = "")
        elif i == 1 and m[i] > 0:
            print(f' +{m[i]}x', end = "")
        elif i == 1:
            print(f' {m[i]}x', end = "")
        elif m[i] > 0:
            print(f' +{m[i]}x^{i}', end = "")
        else:
            print(f' {m[i]}x^{i}', end = "")
            
    
print(" = 0")

