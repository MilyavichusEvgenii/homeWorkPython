import core_model
import translate
def GetNumb(massage: str):
    result = 0
    while True:
        a = int(input(massage))
        if a > 0 and a < 5:
            result = a
            break
    return result

def MenuProg():
    print('Пользователь! Добро пожаловать в телефонный справочник.\n' 
    'Выберете номер команды:\n 1 - ввод данных в базу\n 2 - импорт из файла в базу\n 3 - экспорт базы в файл\n 4 - печать базы в консоль')
    number = GetNumb('Введите номер команды: ')
    if number == 1:
        core_model.Core()
    if number == 2:
        path = input('Введите имя файла с расширениями TXT или CSV: ')
        translate.FileToFile(path, 'base.csv')
    if number == 3:
        path = input('Введите имя файла с расширением TXT или CSV: ')
        translate.FileToFile('base.csv', path)
    if number == 4:
        Print('base.csv')




def Print(data):
    with open(data, 'r', encoding='utf-8') as file:
        result = file.read()
    print(result)