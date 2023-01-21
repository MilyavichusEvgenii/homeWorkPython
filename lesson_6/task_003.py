#Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
import math
def GetNumb():
    result = 0
    while True:
        a = int(input('Введите положительное число, чтоб задать последовательность чисел (1+1/n)**n: '))
        if a > 0:
            result = a
            break
    return result

def MathMethod(a):
    #list = []
    tList = list([math.pow((1 + 1/i), i) for i in range(1, a + 1)])
    #for i in range(1, a + 1):
        #e = math.pow((1 + 1/i), i)
        #list.append(e)
    return tList
def RecSum(a, b):
    count = 0
    if b == len(a):
        return count
    else:
        count+= a[b]
        return RecSum(a, b +1) + count

numbRes = GetNumb()
listRes = MathMethod(numbRes)
sumResult = RecSum(listRes, 0)
print(f'Сумма ряда чисел {listRes} равняется {sumResult}')
