#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).


def GetNumb():
    result = 0
    while True:
        a = int(input('Введите номер четверти координатной плоскости: '))
        if a > 0 and a < 5:
            result = a
            break
        else:
            print('Введите число от 1 до 4')
    return result

def NumbQ(a):
    if a == 1:
        print('X > 0, Y > 0')
    elif a == 2:
        print('X < 0, Y > 0')
    elif a == 3:
        print('X < 0, Y < 0')
    else:
        print('X > 0, Y < 0')

number = GetNumb()
NumbQ(number)





