'''
Последовательностью Фибоначчи называется
последовательность чисел a0, a1, ..., an, ..., где
a0= 0, a1= 1, ak= ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
'''

def Fibonacci(n):
    if n in [0,1]:
        return 1
    return Fibonacci(n-1) + Fibonacci(n-2)

n = int(input("Input: "))
print(f'Output: {Fibonacci(n)}')
