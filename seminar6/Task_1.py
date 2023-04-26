'''
Задача №39. Решение в группах
Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива
Ввод:                           Вывод: 
7                               3 3 2 12              
3 1 3 4 2 4 12
6
4 15 43 1 15 1           (каждое число вводится с новой строки
'''
# First employment

list1 = [int(input(f'{i+1}:')) for i in range(int(input('enter the size of first array: ')))]
print()
list2 = [int(input(f'{i+1}:')) for i in range(int(input('enter the size of second array: ')))]
print()
list3 = [i for i in list1 if i not in list2]

print(list1)
print(list2)
print(list3)

# Second employment

list_1 = list(map(int, input('enter elements of first array: ').split()))
list_2 = list(map(int, input('enter elements of second array: ').split()))
list_3 = [i for i in list_1 if i not in list_2]
print(list_1)
print(list_2)
print(list_3)