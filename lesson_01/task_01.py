#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#Пример:
#- 6 -> да
#- 7 -> да
#- 1 -> нет

def GetNumb():
    result = 0
    while True:
        day = int(input('Введите день недели: '))
        if day > 0:
            result = day
            break
        else:
            print('Вы ввели неверное числовое значение')
    return result

def Day(a):
    if a == 6 or a == 7:
        print(f'{a} день недели является выходным днем.')
    else:
        print(f'{a} день недели не является выходным днем.')

resNumb = GetNumb()
Day(resNumb)