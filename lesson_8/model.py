#Доделать решение задачи: Задача: Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы
import UserI
import viev
from collections import defaultdict
import csv
import json

def InputBase():
    while True:
        name = input('Введите имя: ')
        status = input('Введите название должности: ')
        salary = int(input('Введите размер зарплаты: '))
        with open('main.csv', 'a', encoding='utf-8') as file:
            file.write('{};{};{}\n'
                                .format(name, status, salary))
        if int(input('Если вы хотите продолжить операцию ввода, нажмите 1, в противном случае нажмите 0: ')) == 0:
            break

def FileToFile(pathA, PathB):
    with open(pathA, 'r', encoding='utf-8') as outfile:
        data = outfile.read().split('/n')
        data = list(filter(None, data))
    with open(PathB, 'a', encoding='utf-8') as infile:
        [infile.write(f'{i}\n') for i in data]
        

def DicInit(path):
    dic = defaultdict(dict)
    with open(path, 'r', encoding='utf-8') as file:
        data = file.read().split('\n')
        data = list(filter(None, data))
        for k, i in enumerate(data):
            i = i.split(';')
            temDic = {'name': i[0], 'status': i[1], 'salary': i[2]}
            dic[k].update(temDic)
    return dic

def SearchDic(dic: dict):
    search = input('Введите поисковое значение выборки: ')
    for i in range(len(dic)):
        tempList = list(map(lambda x: x.lower(), list(dic[i].values())))
        if tempList.count(search.lower()) > 0:
            viev.Print(dic[i])

def DelDic(dic: dict):
    delName = input('Введите имя сотрудника для удаления из базы: ')
    for i in range(len(dic)):
        tempList = list(map(lambda x: x.lower(), list(dic[i].values())))
        if tempList[0].count(delName.lower()):
            dic.pop(i)
            WriteDicToMain(dic)
            break

def WriteDicToMain(dic: dict):
    with open('main.csv', 'w', encoding='utf-8') as file:
        for i in dic:
            tempList = list(dic[i].values())
            file.write('{};{};{}\n'
                             .format(tempList[0], tempList[1], tempList[2]))

def ReinitData(dic: dict):
    search = input('Введите имя сотрудника для изменения данных: ')
    pleace = 0
    for i in range(len(dic)):
        tempList = list(map(lambda x: x.lower(), list(dic[i].values())))
        if tempList[0].count(search.lower()) > 0:
            viev.Print(dic[i])
            pleace = i
            break
    number = UserI.GetNum(0, 4, 'Введите команду для изменения:\n 1 - изменить имя\n 2 - изменить должность\n 3 - изменить зарплату: ')
    if number == 1:
        dic[pleace]['name'] = input('Введите новое имя: ')
    if number == 2:
        dic[pleace]['status'] = input('Введите новую должность: ')
    if number == 3:
        dic[pleace]['salary'] = input('Введите новый размер заработной платы: ')
    WriteDicToMain(dic)

def ConvertCsvToJson(pathA, pathB):
    outFile = open(pathA, 'r', encoding='utf-8')
    inFile = open(pathB, 'w', encoding='utf-8')
    reader = csv.DictReader(outFile)
    for i in reader:
        json.dump(i, inFile)
        inFile.write('\n')
    outFile.close()
    inFile.close()

    
