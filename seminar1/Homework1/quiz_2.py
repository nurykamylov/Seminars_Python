"""
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

*Пример:*

6 -> 1  4  1
24 -> 4  16  4
    60 -> 10  40  10
"""
cranes = int(input('Type the number of Cranes: '))
flag = True
while flag:
    if cranes % 6 == 0:
        flag = False
        print(f"{cranes}-> Петя = {cranes//6}, Катя = {cranes//2 + cranes//6}, Сережа = {cranes//6}")
    else:
        flag = False
        print('Wrong number! Try to get correct number ! Hint : number of cranes should be divide to 6 without remains ;)')
