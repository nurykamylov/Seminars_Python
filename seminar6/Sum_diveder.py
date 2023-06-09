'''
Два различных натуральных числа n и m называются
дружественными, если сумма делителей числа n
(включая 1, но исключая само n) равна числу m и
наоборот. Например, 220 и 284 – дружественные числа.
По данному числу k выведите все пары дружественных
чисел, каждое из которых не превосходит k. Программа
получает на вход одно натуральное число k, не
превосходящее 105
. Программа должна вывести все
пары дружественных чисел, каждое из которых не
превосходит k. Пары необходимо выводить по одной в
строке, разделяя пробелами. Каждая пара должна быть
выведена только один раз (перестановка чисел новую
пару не дает).
Ввод:               Вывод:
300                 220 284
'''

def mult(num):
    sum = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            sum += i
    return sum
number = (int(input('Введите число: ')))
for i in range(number):
    j = mult(i)
    if i < j < number and i == mult(j):
        print(i, j)

                    # Second employment
                
# Два различных натуральных числа n и m
# называются дружественными, если сумма
# делителей числа n (включая 1, но исключая само n)
# равна числу m и наоборот. Например, 220 и 284 – дружественные числа.

# все делители числа 284
# 220 = 1 + 2 + 4 + 71 + 142
# все делители числа 220
# 284 = 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110

# https://ru.stackoverflow.com/questions/1348243/

def pair(value):
    # Получаем корень числа, отбрасываем дробную часть
    sq_num = int(value ** 0.5)

    # Выставляем начальное значение в переменной
    # Если переменная sq_num возведённая в квадрат
    # не равна полученному числу, прибавляем 0.
    # Иначе прибавляем это число, т.к. оно тоже множитель
    res = 1 + (0 if sq_num ** 2 != value else sq_num)

    # Цикл от 2 др корня числа
    for i in range(2, sq_num):

        # Если полученное число делиться на i без остатка
        if value % i == 0:

            # Складываем в переменную значение i
            # и второй делитель, например
            # value = 10, i = 2, второй делитель 5
            res += i + value // i
    return res


for j in range(10, 300):
    # Первое число, это сумма множителей j
    sum1 = pair(j)

    # Второе число, это сумма множителей sum1
    sum2 = pair(sum1)

    # Если второе число равно j и первое число меньше второго
    # Второе условие защита от дубликатов,
    # записанных наоборот
    if sum2 == j and sum1 < sum2:
        print(j, sum1)