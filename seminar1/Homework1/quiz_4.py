'''
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

*Пример:*

3 2 4 -> yes
3 2 1 -> no
'''
print('Enter the area of chocolate')
n = int(input('n = '))
m = int(input('m = '))
print('Enter the part of chocolate')
k = int(input('k = '))

if (k%m == 0 or k%n == 0) and k < n*m:
    print("yes!")
else:
    print('no!')
