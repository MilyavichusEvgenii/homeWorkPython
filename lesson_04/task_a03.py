#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
from random import randint
def SizeList(str):
    result = 0
    while True:
        a = int(input(str))
        if a > 0:
            result = a
            break
    return result

def InitList(a):
    tempList = []
    for i in range(a):
        while True:
            r = randint(1, 9)
            if i == 0:
                tempList.append(r)
                break
            elif tempList[i - 1] != r:
                tempList.append(r)
                break      
    return tempList

numb = SizeList('Введите длину списка чисел: ')
resList = InitList(numb)
print(f'Список неповторяющихся элементов: {resList}')