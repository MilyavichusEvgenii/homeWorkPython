#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в отдельном списке( пример n=4, lst1=[4,-2,1,3] - списко на основе n, а позиции элементов lst2=[3,1].
import re
def GetNumber():
    result = 0
    while True:
        number = int(input('Введите длину списка: '))
        if number > 0:
            result = number
            break
    return result
def GetPlaceNumb():
    possition = input('Введите множители для множеста из списка через запятую или пробел: ')
    listStr = re.split(',| ', possition)
    data = list(filter(None, listStr))
    result = [int(item) for item in data]
    return result
def MassLine(a):
    lisMass = []
    for i in range(-a, a + 1):
        lisMass.append(i)
    return lisMass
def MultipleMass(a, b):
    resLis = []
    path = 'file.txt'
    r: str = ""
    temp = 0
    for i in b:
        with open(path, 'a') as data:
                data.writelines('\n')
        for k in range(len(a)):
            resLis.append(i*k)
            temp = i*a[k]
            if(k == (len(a) -1)):
                r = str(temp)
            else:
                r = str(temp) + ", "
            with open(path, 'a') as data:
                data.write(f'{r} ')
def PrintData():
    print('Чтение результата работы программы из файла "file.txt')
    path = 'file.txt'
    data = open(path).readlines()
    for line in data:
        if not line.isspace():
            print(line.replace('\n', ''))
    data = open(path, 'w')
    data.write('')
    data.close()
    





size = GetNumber()
mult = GetPlaceNumb()
multSize = MassLine(size)
MultipleMass(multSize, mult)
print(f'Множество {multSize} будет поочередно перемножено на множество {mult}')
PrintData()