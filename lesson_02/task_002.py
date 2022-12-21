#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#Пример: - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def GetNumb():
    result = 0
    while True:
        strNumb = int(input('Введите число от 1 до N: '))
        if strNumb > 0:
            result = strNumb
            break
    
    return result

def FNumb(a):
    if a == 0 or a == 1:
        return 1
    else:
        return a*FNumb(a - 1)

number = GetNumb()
resNumb = FNumb(number)
print(f'Факториал числа {number} равняется {resNumb}')
        