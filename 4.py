# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input('Введите десятичное число '))

def binary_num(n):
    quotient = n
    remind = 0
    binary_digit = ''
    while quotient != 0:
        remind = quotient % 2
        quotient = quotient // 2
        binary_digit = binary_digit + str(remind)
    return binary_digit[::-1]

numbers = binary_num(num)
print(numbers)
