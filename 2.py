# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
try:

    n = int(input("Введите количество элементов: "))  
    created_list = []
    for i in range(n):
        created_list.append(int(input(f"Введите {i + 1} элемент: ")))
    print(f'Исходный список{created_list}')
except:
    print("Введите целое число")

def pair_of_num(lst):
  num = []
  size = len(lst)
  circle = int(size / 2)
  if size % 2 == 0:
    for i in range(circle):
        num.append(lst[i] * lst[size - 1 - i])
    return num
  else:
    for i in range(circle):
        num.append(lst[i] * lst[size - 1 - i])
  num.append(lst[circle]**2)
  return num
  
new_list = pair_of_num(created_list)
print(f'Список произведения пар чисел {new_list}')