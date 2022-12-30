#Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import runpy


def MethFile(str):
    runpy.run_path('task_a04.py')
    path = "FileTask_a04.txt"
    temp = ""
    with open(path, 'r') as data:
        for i in data:
            temp = temp + i

    with open(str, 'a') as file:
        for i in temp:
            file.write(i)
    
    with open(path, 'w') as old:
        old.write("")

def OpenFile(str):
    tempOne = ""
    with open(str, 'r') as resOne:
        for i in resOne:
            tempOne = tempOne + i
    return tempOne

def SumFiles(str):
    expOne = OpenFile("file_01_a05.txt")
    expTwo = OpenFile("file_02_a05.txt")
    tempList = []
    newexpOne = expOne.replace(" = 0", " + ")
    tempList.append(newexpOne)
    tempList.append(expTwo)
    battary: str = ""
    for i in range(len(tempList)):
        for j in tempList[i]:
            battary = battary + j
        
    with open(str, 'a') as resFile:
        for i in battary:
            for j in i:
                resFile.write(j)

def ClearData(str):
    with open(str, 'w') as temp:
        temp.write('')

def ClinFiles(a, b, c):
    ClearData(a)
    ClearData(b)
    ClearData(c)

def PrintIntoFile(str):
    mas = ""
    with open(str, 'r') as item:
        for i in item:
            mas = mas + i

    print(f'Информация выгруженная из файла {str}: {mas}')


ClinFiles("file_01_a05.txt", "file_02_a05.txt", "ResultFile_a05.txt")
MethFile("file_01_a05.txt")
MethFile("file_02_a05.txt")
SumFiles("ResultFile_a05.txt")
PrintIntoFile("ResultFile_a05.txt")




