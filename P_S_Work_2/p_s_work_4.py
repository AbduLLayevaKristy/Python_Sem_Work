"""
Задача 4: 
Задайте список из N элементов, заполненных числами 
из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
3 -> [2, 3, -3, -2, -1, 0, 1]
"""

length = int(input('Введите длину массива: '))
nums = list(map(int, input('Введите числа промежуток [-N,N]: ').split()))
shift = int(input('На сколько позиций сдвинуть: '))

lst = nums[-shift:] + nums[:-shift]

print(lst)