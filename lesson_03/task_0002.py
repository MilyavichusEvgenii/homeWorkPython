#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]
from random import randint
def GetNum():
    result = 0
    while True:
        a = int(input('Введите длину массива: '))
        if a > 0:
            result = a
            break
    return result

def GetList(a):
    tempList = []
    for i in range(a):
        tempList.append(randint(1, 10))
    return tempList

def SummList(a):
    tempList = []
    summ = 0
    for i in range(len(a)):
        if i == (len(a) - 1 - i):
            summ = a[i] + a[len(a) - 1 - i]
            tempList.append(summ)
            break
        elif i > (len(a) - 1 - i):
            break
        else:
            summ = a[i] + a[len(a) - 1 - i]
            tempList.append(summ)
    return tempList

numb = GetNum()
resList = GetList(numb)
resSumList = SummList(resList)
print(f'Изначальный список: {resList} и список суммы пар чисел, взятых симметрично слева и справа изначального списка: {resSumList}')