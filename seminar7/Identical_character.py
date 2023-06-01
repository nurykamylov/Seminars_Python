"""
Напишите функцию same_by(characteristic, objects), которая
проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так.
Если значение характеристики для разных объектов
отличается - то False. Для пустого набора объектов, функция
должна возвращать True. Аргумент characteristic - это
функция, которая принимает объект и вычисляет его
характеристику.
Ввод:                                           Вывод:
values = [0, 2, 10, 6]                              same
if same_by(lambda x: x % 2, values):
    print(‘same’)
else:
    print(‘different’)
"""

values = [1, 3, 7,9]    
def same_by(f,a):
    t = bool
    if a[0] %2==0: 
        for i in a:
            if f(i) == 0:
                t = True
            else:
                return False
    else:
        for i in a:
            if f(i) != 0:
                t = True
            else:
                return False
    return t
                            
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')


# second employment 
values = [1, 3, 9, 5, 7]
def same_by(f,a):
    return len(set(list(map(f,a))))==1

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')