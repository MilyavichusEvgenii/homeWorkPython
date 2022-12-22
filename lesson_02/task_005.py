#Реализуйте алгоритм перемешивания списка. (рандомно поменять местами элементы списка между собой)
import random
def GivNumb():
    result = 0
    while True:
        a = int(input('Введите размер списка: '))
        if a > 0:
            result = a
            break
    return result
def GiveList(a):
    tempList = []
    for i in range(1, a + 1):
        tempList.append(i)
    return tempList
def RandReplace(a):
    random.shuffle(a)

number = GivNumb()
listNumb = GiveList(number)
RandReplace(listNumb)
print(f'Список со случайным распределением элементов от 1 до N: {listNumb}')