#Создайте программу для игры в ""Крестики-нолики"".
from random import randint
def GetNumb(massage):
    result = 0
    while True:
        a = int(input(massage))
        if a > 2 and a < 10 and a % 2 == 1:
            result = a
            break
    return result

def InitMap(a, b):
    tempList = [[b] * a for i in range(a)]
    return tempList

def PrintMap(list):
    battary = ""
    for i in range(len(list)):
        if i == 0:
            battary = battary + '  ' + str(i + 1)
        else:
            battary = battary + ' ' + str(i + 1)
    print(battary)
    for i, r in enumerate(zip(*list)):
        print(i + 1, end=' ')
        print(*r, sep=' ')

def Game(map, human, computer, empty):
    count = 0
    while True:
        xrh = 0
        yrh = 0
        xrp = 0
        yrp = 0
        count = count + 2
        while True:
            print(f"Ход человека {count}")
            (xr, yr) = TapeHuman(map, human, computer, empty)
            xrh = xr
            yrh = yr
            PrintMap(map)
            break
        if WinGame(map, human, xrh, yrh) == 1:
            print("Человек выйграл")
            break
        if count == 10:
            print("Ничья. Игра окончена.")
            break
        while True:
            print(f"Ход компьютера")
            (xrс, yrс) = TapeComputer(map, human, computer, empty)
            xrp = xrс
            yrp = yrс
            PrintMap(map)
            break
        if WinGame(map, computer, xrp, yrp) == 1:
            print("Kомпьютер выиграл")
            break
        
        
        

def TapeHuman(map, human, computer, empty):
    xr = 0
    yr = 0
    while True:
        while True:
            a = int(input("Введите числовое значение для X координатной плоскости: "))
            if a >= 0 and a <= (len(map)):
                x = a
                xr = a
                break
        while True:
            b = int(input("Введите числовое значение для Y координатной плоскости: "))
            if b >= 0 and b <= (len(map)):
                y = b
                yr = b
                break
        if map[x - 1][y - 1] == empty:
            map[x - 1][y - 1] = human
            break
        else:
            print("Позиция занята")
    return (xr - 1, yr - 1)


def TapeComputer(map, human, computer, empty):
    xr = 0
    yr = 0
    while True:
        x = randint(0, (len(map) - 1))
        y = randint(0, (len(map) - 1))
        if map[x][y] == empty:
            map[x][y] = computer
            xr = x
            yr = y
            break
    return (xr, yr)

def WinGame(map, char, xr, yr):
    if Horizontal(map, char, xr, yr) == 1:
        return 1
    elif Vertical(map, char, xr, yr) == 1:
        return 1
    elif Diagonal(map, char, xr, yr) == 1:
        return 1

def Horizontal(map, char, xr, yr):
    result = 0
    if xr == 0:
        if map[xr][yr] == char and map[xr + 1][yr] == char and map[xr + 2][yr] == char:
            result = 1
    elif xr == (len(map) - 1):
        if map[xr][yr] == char and map[xr -1][yr] == char and map[xr - 2][yr] == char:
            result = 1 
    elif xr > 0 and xr < (len(map) - 1):
        if map[xr - 1][yr] == char and map[xr][yr] == char and map[xr + 1][yr] == char:
            result = 1
    
    return result

def Vertical(map, char, xr, yr):
    result = 0
    if yr == 0:
        if map[xr][yr] == char and map[xr][yr + 1] == char and map[xr][yr + 2] == char:
            result = 1
    elif yr == (len(map) - 1):
        if map[xr][yr] == char and map[xr][yr - 1] == char and map[xr][yr - 2] == char:
            result = 1 
    elif yr > 0 and yr < (len(map) - 1):
        if map[xr][yr - 1] == char and map[xr][yr] == char and map[xr][yr + 1] == char:
            result = 1 
    return result

def Diagonal(map, char, xr, yr):
    result = 0
    if xr == 0 and yr == 0:
        if map[xr][yr] == char and map[xr + 1][yr + 1] == char and map[xr + 2][yr + 2] == char:
            result = 1
    elif xr == (len(map) - 1) and yr == (len(map) - 1):
        if map[xr][yr] == char and map[xr - 1][yr - 1] == char and map[xr - 2][yr - 2] == char:
            result = 1 
    elif xr == (len(map) - 1) and yr == 0:
        if map[xr][yr] == char and map[xr - 1][yr + 1] == char and map[xr - 2][yr + 2] == char:
            result = 1 
    elif xr == 0 and yr == (len(map) - 1):
        if map[xr][yr] == char and map[xr + 1][yr - 1] == char and map[xr + 2][yr - 2] == char:
            result = 1
    #elif xr > 0 and xr < (len(map) - 1) or yr > 0 and yr < (len(map) - 1):
        #if map[xr - 1][yr - 1] == char and map[xr][yr] == char and map[xr + 1][yr + 1] == char:
            #result = 1 
    return result

n = GetNumb("Введите нечетное число больше двух и меньше десяти для инициализации размера поля: ")
charEmpty = '*'
charHuman = 'x'
charComputer = '0'
mapList = InitMap(n, charEmpty)
PrintMap(mapList)
Game(mapList, charHuman, charComputer, charEmpty)
