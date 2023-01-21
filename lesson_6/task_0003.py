#Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# (если получаются длинные числа после запятой, это нормально и особенность данного языка программирования. 
# ваш ответ может не совпадать с примером(может получитя 0,20)) Пример:- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random
import functools
from functools import reduce
def GetNumber():
    result = 0
    while True:
        a = int(input('Введите длину списка: '))
        if a > 0:
            result = a
            break
    return result

def InitList(a):
    tempList = [round(random.uniform(1, 10), 2) for i in range(a)]
    #tempList = []
    #temp = 0
    #for i in range(a):
    #    temp = round(random.uniform(1, 10), 2)
    #    tempList.append(temp)
    return tempList

def DifMinMax(a):
    tempList =[]
    tempList = sorted(a)
    result = tempList[-1] - tempList[0]
    return int(result * 100) / 100

numb = GetNumber()
getList = InitList(numb)
resultDif = DifMinMax(getList)
print(f'Разница между максимальным и минимальным элементами списка: {getList} равна {resultDif}')
