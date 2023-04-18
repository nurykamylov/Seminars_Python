'''
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  
строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    3
    -> 1

'''
from random import randint

low_bound = int(input("low_bound: "))
high_bound = int(input('high bound: '))
k = int(input('quantity: '))
list = [randint(low_bound, high_bound) for i in range(k)]

print(list)

t  =  int(input('Enter the number: '))
count = 0
for i in range(len(list)):
    if t == list[i]:
        count +=1
print(f"count of number = {count}")