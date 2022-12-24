#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#Пример:
#- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 


def GetNumb():
    result = 0
    while True:
        a = int(input('Введите длину ряда чисел Фибоначчи: '))
        if a > 0:
            result = a
            break
    return result

def initRecList(a):
    if a == 1:
        return
    for i in range(2, a + 1):
        e = Fibo(i)
        resList.append(e)
        resList.insert(0, -e)

def Fibo(a):
    if a == 1: 
        return 0
    elif a == 2:
        return 1
    else:
        return Fibo(a - 1) + Fibo(a - 2)
        

resList = [0]
numb = GetNumb()
initRecList(numb)
print(f'Ряд чисел Фибоначчи {resList} из {numb} элементов')
