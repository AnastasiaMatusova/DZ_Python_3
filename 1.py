# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

lst = list(map(int, input("Введите числа через пробел:\n").split()))
lst2 = []
for i in range(len(lst)):
    lst[i] = int(lst[i])
    if(i) % 2 != 0:
        lst2.append(lst[i])
print(f'На нечетных позициях у нас есть следующие элементы : {lst2}')
print(f'Сумма элементов {lst2} равна : {sum(lst2)}')