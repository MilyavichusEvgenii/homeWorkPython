#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Пример:
#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10

def GetNumb():
    result = 0
    while True:
        a = int(input('Введите число: '))
        if a > 0:
            result = a
            break
    return result

def RecNumb(a):
    if a == 0:
        return 1
    else:
        temp = a % 2
        recList.append(temp)
        RecNumb(a // 2)

recList = []
numb = GetNumb()
RecNumb(numb)
recList.reverse()
print(f'Число {numb} в десятичной системе счисления при переводе в двоичную равняется {recList}')
