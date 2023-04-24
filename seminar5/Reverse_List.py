'''
Дано натуральное число N и
последовательность из N элементов.
Требуется вывести эту последовательность в
обратном порядке.

Примечание. В программе запрещается
объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3
'''
 # первая реализация
list = list(map(int, input('erter the elements: ').split()))
print(*list.__reversed__())
print(list[::-1])

# вторая реализация

def reverse(n):
    if n < 1:
        return ""
    res = input('enter numbers:')
    return reverse(n-1) + f'{res} '
print(reverse(5))
