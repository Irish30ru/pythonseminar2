Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


number_N = int(input('Введите количество элементов списка: '))

nums = []
value = 1
for i in range(1, number_N + 1):
    nums.append(value)
    value *= i + 1
print(nums)




Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
3 -> [2, 3, -3, -2, -1, 0, 1]

from random import randint
numbers = []
for i in range(10):
    numbers.append(randint (-10,10))
print(numbers)

def get_numbers(numbers):
    count =0 
    for element in numbers:
        count +=1
    return count
print('Number of elements: ', get_numbers(numbers))

x = int(input('Enter  position of first element: '))
y = int(input('Enter position of second element: '))

for i in range(len(numbers)):
    mult = numbers[x -1]*numbers[y - 1]
print(f'Mult of elements: {numbers[x -1]} * {numbers[y -1]} =', mult)