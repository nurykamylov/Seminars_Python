'''
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

'''

string  = "a a a b a a c d c d d".split()

dict = {}.fromkeys(string,0)

for i in string:
    if dict[i] != 0:                              #
        print(f'{i}_{dict[i]}', end=" ")          #  Тирнарный оператор:
    else:                                         #      print(f'{i}_{dict[i]}' if dict[i] else i ,end=" ")    
        print(i, end=" ")                         #  
    dict[i] +=1