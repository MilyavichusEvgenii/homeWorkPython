#Вычислить число c заданной точностью d
#Пример:
#- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

def GetNumb(str):
    result = 0
    while True:
        number = float(input(str).replace(',', '.'))
        if(number >= 0 or number <= 0):
            result = number
            break
    return result

def MathNubm(a, b):
    r = a / b
    d = a / b
    count = 0
    while d % 1 != 0:
        d = d * 10
        count+=1
    return (r, count)

def ResNumb(a, b, str):
    resSize = 0
    while True:
        c = int(input(str))
        if c >= 0 and c <= b:
            resSize = c
            break
    
    if resSize > 0 and resSize < 15:
        result = int(a * 10 ** resSize) / 10 ** resSize
    elif resSize == 15:
        result = int(a)
    else:
        result = a 
   
    return (result, resSize, )

a = GetNumb('Введите делимое: ')
b = GetNumb('Введите делитель: ')
(numbFloat, size, ) = MathNubm(a, b)
print(f'Частное от деления делимого {a} на делитель {b} равняется {numbFloat} с {size} знаками после запятой')
(resultNumb, devSize, ) = ResNumb(numbFloat, size, f'Определите точность дробного значения в виде количества разрядов после запятой <= {size}: ')
print(f'Число {numbFloat} с {size} разрядами послезапятой с точностью до {devSize} после запятой равняется {resultNumb}')







