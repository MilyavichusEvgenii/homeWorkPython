#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#a) Добавьте игру против бота
#b) Подумайте как наделить бота ""интеллектом""
from random import randint

def GetNumb(a, massage):
    result = 0
    while True:
        b = int(input(massage))
        if b >= a:
            result = b
            break
    return result

def GetNumbDuf(a, massage):
    result = 0
    while True:
        b = int(input(massage))
        if b >= 1 and b <= 2:
            result = b
            break
    return result

def HumanComputerGame(sweets, tape, difficult):
    r = randint(1, 2)
    if difficult == 1:
        LightGame(sweets, tape)
    elif difficult == 2:
        if r == 1:
            print("Первым ходит человек")
            HardGame(sweets, tape)
        else:
            print("Первым ходит компьютер")
            HardGameInvers(sweets, tape)

               
def LightGame(sweets, tape):
    rand = randint(0, 1)
    param = 0
    while True:
        while True:
            a = TapeHuman(sweets, tape)
            sweets = sweets - a
            print(f"Конфет осталось после человека {sweets}. Человек взял на этом ходу {a} конфет")
            param = 1
            break
        if sweets == 0 and param == 1:
            print("Победил человек")
            break
        
        while True:
            b = TapeComputer(sweets)
            sweets = sweets - b
            print(f"Конфет осталось после компьютера {sweets}. Компьютер взял на этом ходу {b} конфет")
            param = 2
            break
        if sweets == 0 and param == 2:
            print("Восстание машин свершилось. Победил компьютер")
            break

def HardGame(sweets, tape):
    param = 0
    count = 0
    while True:
        while True:
            a = TapeHuman(sweets, tape)
            sweets = sweets - a
            count = count + 1
            print(f"Конфет осталось после человека {sweets}. Человек взял на этом ходу {a} конфет. Ход {count}")
            param = 1
            break
        if sweets == 0 and param == 1:
            print("Победил человек")
            break
        
        while True:
            b = HardComputer(sweets, tape, count)
            sweets = sweets - b
            count = count + 1
            print(f"Конфет осталось после компьютера {sweets}. Компьютер взял на этом ходу {b} конфет. Ход {count}")
            param = 2
            break
        if sweets == 0 and param == 2:
            print("Восстание машин свершилось. Победил компьютер")
            break


def HardGameInvers(sweets, tape):
    param = 0
    count = 0
    while True:
        while True:
            b = HardComputer(sweets, tape, count)
            sweets = sweets - b
            count = count + 1
            print(f"Конфет осталось после компьютера {sweets}. Компьютер взял на этом ходу {b} конфет. Ход {count}")
            param = 2
            break
        if sweets == 0 and param == 2:
            print("Восстание машин свершилось. Победил компьютер")
            break

        while True:
            a = TapeHuman(sweets, tape)
            sweets = sweets - a
            count = count + 1
            print(f"Конфет осталось после человека {sweets}. Человек взял на этом ходу {a} конфет. Ход {count}")
            param = 1
            break
        if sweets == 0 and param == 1:
            print("Победил человек")
            break      


def TapeComputer(c):
    result = 0
    while True:
        r = randint(0, 28)
        if r <= c:
            result = r
            break
    return result

def HardComputer(sweets, tape, count): 
    r = 0
    if sweets % tape > 0:
        if sweets > 56:
            r = sweets % tape
        elif sweets < 56 and sweets > 28:
            r = (sweets % tape) - 1
    if sweets == 56:
        r = 1
    if sweets <= 28:
        r = sweets
    return r
    
def TapeHuman(c, d):
    result = 0
    print("Ходит человек:")
    while True:
        a = int(input("Сколько конфет будет взято?: "))
        if a >= 0 and a <= c and a <= d:
            result = a
            break  
    return result

min = 84
option = 2
sweets = GetNumb(min, "Введите число больше либо равно 84: ")
difficult = GetNumbDuf(option, "Введите уровень сложности: 1 - легко, 2 - тяжело: ")
tape = 28

HumanComputerGame(sweets, tape, difficult)
