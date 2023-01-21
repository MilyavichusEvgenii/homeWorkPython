#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


def GetWriteMass():
    mass = input('Введите текст: ')
    for i in mass:
        with open('input.txt', 'a') as data:
            data.write(i)
    

def GetReadMass(path):
    battary = ''
    data = open(path, 'r').readlines()
    for i in data:
        battary = battary + i
    return battary
        


def RleMethod(massage):
    encoding = ''
    mainChar = ''
    count = 1

    if not massage: return
    for char in massage:
        if char != mainChar:
            if mainChar:
                encoding += str(count) + mainChar
            count = 1
            mainChar = char
        else:
            count += 1
    else:
        encoding += str(count) + mainChar
        with open('tempput.txt', 'a') as data:
            data.writelines(encoding)
        return encoding

def RleDecode(massage: str ):
    decode = ''
    count = ''
    for char in massage:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    with open('output.txt', 'a') as data:
        data.writelines(decode)




GetWriteMass()
massRes = GetReadMass('input.txt')
res = RleMethod(massRes)
RleDecode(res)
tempput = GetReadMass('tempput.txt')
output = GetReadMass('output.txt')
print(f'Входные данные, полученные из файла "input.txt": {massRes}')
print(f'Кодированные данные, полученные из файла "tempput.txt": {tempput}')
print(f'Декодированные данные, полученные из файла "output.txt": {output}')

