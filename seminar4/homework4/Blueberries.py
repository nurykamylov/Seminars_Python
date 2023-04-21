'''
В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
круглой грядке, причем кусты высажены только по окружности. Таким образом, у
каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai
 ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.
4 -> 1 2 3 4
9
'''

k = int(input('lower register: '))
n = int(input('higher register: '))
m = int(input('size of list: '))
from random import randint
list = [randint(k,n) for i in range(m)]
print(list)
k = int(input("Enter the number: "))
sum1 = 0
sum2 = 0
sum3 = 0
if k in list:
    for i in range(len(list)):
        if k == list[-1]:
            if list[-3] + list[-2] + list[-1] >= list[-1] + list[0] + list[1]:
                sum1 = list[-3] + list[-2] + list[-1]
            elif list[-3] + list[-2] +list[-1] < list[-1] + list[0] + list[1]:
                sum1 = list[-1] + list[0] + list[1]
            if list[-2] + list[-1] + list[0] >= list[-1] +list[0] + list[1]:
                sum2 = list[-2] + list[-1] + list[0]
            elif list[-2] + list[-1] + list[0] < list[-1] + list[0] + list[1]:
                sum2 = list[-1] + list[0] + list[1]
            if list[-3] + list[-2] + list[-1] >= list[-2] + list[-1] + list[0]:
                sum3 = list[-3] + list[-2] + list[-1]
            elif list[-3] + list[-2] + list[-1] < list[-2] + list[-1] + list[0]:
                sum3 = list[-2] + list[-1] + list[0]
            break
        if k == list[-2]:
            if list[-4] + list[-3] + list[-2] >= list[-2] + list[-1] + list[0]:
                sum1 = list[-4] + list[-3] + list[-2]
            elif list[-4] + list[-3] + list[-2] < list[-2] + list[-1] + list[0]:
                sum1 = list[-2] + list[-1] + list[0]
            if list[-3] +list[-2] + list[-1] >= list[-2] + list[-1] + list[0]:
                sum2 = list[-3] +list[-2] + list[-1]
            elif list[-3] +list[-2] + list[-1] < list[-2] + list[-1] + list[0]:
                sum2 = list[-2] + list[-1] + list[0] 
            if list[-4] + list[-3] + list[-2] >= list[-3] +list[-2] + list[-1]:
                sum3 = list[-4] + list[-3] + list[-2]
            elif list[-4] + list[-3] + list[-2] < list[-3] +list[-2] + list[-1]:
                sum3 = list[-3] +list[-2] + list[-1]
            break
        if k == list[i]:
            if list[i-2] + list[i-1] + list[i] >= list[i] + list[i+1] + list[i+2]:
                sum1 = list[i-2] + list[i-1] + list[i]
            elif list[i-2] + list[i-1] + list[i] < list[i] + list[i+1] + list[i+2]:
                sum1 = list[i] +list[i+1] + list[i+2]
            if list[i-1] + list[i] + list[i+1] >= list[i] +list[i+1] + list[i+2]:
                sum2 = list[i-1] + list[i] + list[i+1]
            elif list[i-1] + list[i] + list[i+1] < list[i] + list[i+1] + list[i+2]:
                sum2 = list[i] + list[i+1] + list[i+2]
            if list[i-2] + list[i-1] + list[i] >= list[i-1] + list[i] + list[i+1]:
                sum3 = list[i-2] + list[i-1] + list[i]
            elif list[i-2] + list[-1] + list[i] < list[i-1] + list[i] + list[i+1]:
                sum3 = list[i-1] + list[i] + list[i+1]
else:
    print("nothing found")
print(max(sum1,sum2,sum3))