'''
Дан список чисел. Определите, сколько в нем
встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
'''
n = int(input('Enter the size of list: '))
list_num = [input("enter the number: ") for i in range(n)]
print(len(set(list_num)))