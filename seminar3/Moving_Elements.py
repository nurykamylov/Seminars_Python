'''
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
'''

n = int(input('Enter the size of List: '))
list_num = [input('Enter the elements:') for i in range(n)]
print(list_num)
k = int(input('k= '))
for i in range(k):
    list_num.insert(i,list_num.pop())

print(list_num)