#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def GetNumber(str):
    
    a = int(input(str))
    return a

def DiffNumb(a):
    tempList = []
    size = abs(a)
    for i in range(1, size + 1):
        if a % i == 0:
            tempList.append(i)
    return tempList
        

numb = GetNumber('Введите число: ')
resList = DiffNumb(numb)
print(f'Список простых множителей числа {numb}: {resList}')