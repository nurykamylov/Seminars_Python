'''
Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного
максимума)
Ввод: [-5, 9, 0, 3, -1, -2, 1,
4, -2, 10, 2, 0, -9, 8, 10, -9,
0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]
'''
n = int(input("enter the lower reggistr: "))
m = int(input("enter the higher reggistr: "))
list = list(map(int, input("enter elements: ").split()))
print(list)
res = [i for i in range(len(list)) if list[i] > n and list[i] ]
print(res)