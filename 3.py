# Задача 3. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

try:
    n = int(input("Введите количество вещественных чисел: "))  
    created_list = []
    for i in range(n):
        created_list.append(float(input(f"Введите {i + 1} элемент: ")))
    print(f'Исходный список{created_list}')
except:
    print("Введите вещественное число")

def fractional_part(lst):
    fract_list = []
    int_part = 0
    size = len(lst)
    for i in range(size):
        int_part = int(lst[i])
        fract_part = lst[i] - int_part
        fract_part = round(fract_part,10)
        if fract_part != 0:
            fract_list.append(fract_part)
    try:    
        max = fract_list[0]
        min = fract_list[0]
        for j in range(len(fract_list)):
            if fract_list[j] > max:
                max = fract_list[j]
            elif fract_list[j] < min:
                min = fract_list[j]
        return (max - min)
    except:
        print('Дробные части равны нулю')

new_list = fractional_part(created_list)
print(f'Разница между максимальным и минимальным значением дробной части равна  {new_list}')
