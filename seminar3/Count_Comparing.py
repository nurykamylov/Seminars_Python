'''
Дан массив, состоящий из целых чисел. Напишите
программу, которая подсчитает количество
элементов массива, больших предыдущего (элемента
с предыдущим номером)
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)
'''

                    # First employment
new_list = [int(input()) for i in range(5)]
print(new_list)
count = 0
for i in range(1,len(new_list)):
    if new_list[i-1] < new_list[i]:
        count+=1

print(count)

                    # Second Employment
list_nums = [0, -1, 5, 2, 3]
res = [list_nums[i] > list_nums[i - 1] for i in range(1, len(list_nums))]
print(sum(res))