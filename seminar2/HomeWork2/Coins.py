''''
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх 
одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
5->1 0 1 0 1 1
2
'''
n = int(input('Enter the value of coins: '))
count = 0
count_2 = 0
for i in range(n):
    side = int(input('Enter the side of coin: '))
    while side < 0 or side > 1:
        side = int(input('Enter the corect form of side(1 or 0) : '))
        if side == 0 or side == 1:
            break
    if side == 0:
        count+=1
    else:
        count_2+=1 
if count > count_2:
    print(count_2)
else:
    print(count)
