#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from random import randint
def GetNum():
    result = 0
    while True:
        a = int(input('Введите длину массива: '))
        if a > 0:
            result = a
            break
    return result

def GivList(a):
    inList = []
    for i in range(a):
        inList.append(randint(1, 10))
    return inList

def SumPoss(a):
    summ = 0
    for i in range(len(a)):
        if i % 2 != 0:
            summ+= a[i]
    return summ

size = GetNum()
resList = GivList(size)
battary = SumPoss(resList)
print(f'Сумма нечетных элементов списка {resList} равна {battary}')