#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#Пример:
#- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint
def GetNumber(str):
    result = 0
    while True:
        a = int(input(str))
        if a >= 0 or a <= 0:
            result = a
            break
    return result

def InitListK(a, b):
    tempList = []
    for i in range(a):
        while True:
            r = randint(0, b)
            if i == 0:
                tempList.append(r)
                break
            elif tempList[i - 1] != r:
                tempList.append(r)
                break
    return tempList
       
def BuildString(a, b):
    letter = "x"
    tempList = []
    for i in range(len(a)):
        tempList.append(str(a[i]) + "x" + "**" + str(b[i]))
    return tempList

def CheckList(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j - 1] == '*' and a[i][j] == '0':
                a[i] = 1
    return a

def DelNumb(a: list):
    count = 0
    for i in range(len(a)):
        text = str(a[i])
        countNull = text.count('0x')
        if countNull > 0:
            a[i] = 0
        if a[i] == 1:
            count+=1
    a.append(count)
    tempList = []
    for i in range(len(a)):
        if a[i] != 0 and a[i] != 1:
            tempList.append(a[i])
    return tempList

def PrintResult(a: list):
    massage = ""
    for i in range(len(a)):
        if i == (len(a) - 1):
            massage = massage + str(a[i]) + " = 0"
        else:
            massage = massage + str(a[i]) + " + "
    temp = massage.replace("**1", "")
    newTemp = temp.replace("1x", "x")
    return newTemp

def WriteInFile(mass):
    path = "FileTask_a04.txt"
    with open(path, 'a') as data:
        data.writelines(mass)

def CleanFile(str):
    with open(str, 'w') as temp:
        temp.write('')

        
CleanFile("FileTask_a04.txt")
size = GetNumber('Длину выражения: ')
value = GetNumber('Введите параметр K: ')
numListK = InitListK(size, value)
numListK.sort(reverse=True)
numbersList = InitListK(size, 10)
strList = BuildString(numbersList, numListK)
ChList = CheckList(strList)
Dlist = DelNumb(ChList)
massRes = PrintResult(Dlist)
WriteInFile(massRes)
print(f'Многчлен в степени {value}: {massRes}')