# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1,2,4,8

n = int(input('N= '))
t = 2 
for i in range(n):
    print(t)
    t = t * 2
    if t > n:
        break