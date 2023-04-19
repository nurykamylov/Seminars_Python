'''
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5

'''
from random import randint

low_bound = int(input("low_bound: "))
high_bound = int(input('high bound: '))
k = int(input('quantity: '))
list = [randint(low_bound, high_bound) for i in range(k)]

print(list)

t  =  int(input('Enter the number: '))
new_list =[ list[i]  for i in range(len(list)) if list[i] < t]
new_list1 = [ list[i]  for i in range(len(list)) if list[i] > t] 


if t - max(new_list) <= min(new_list1) -t:
    print(f' closest value: {max(new_list)}')
else:
    print(f' closest value: {min(new_list1)}')