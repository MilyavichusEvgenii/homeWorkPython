import model
import viev

def GetNum(a, b, massage):
    result = 0
    while True:
        numb = int(input(massage))
        if numb > a and numb < b:
            result = numb
            break
    return result


def MenuProg(pathMain, pathRes):
    number = GetNum(0, 9, 'Введите команду для работы с информационной системой:\n1 - найти сотрудника по имени, должности или зарплате\n'
    '2 - добавить сотрудника\n3 - удалить сотрудника\n4 - обновить данные сотрудника\n'
    '5 - экспортировать данные в формате json\n6 - экспортировать данные в формате txt или csv\n'
    '7 - вывод базы сотрудников на экран\n8 - закончить работу программы: ')
    if number == 1:
        dic = model.DicInit(pathMain)
        model.SearchDic(dic)
    if number == 2:
        model.InputBase()
    if number == 3:
        dic = model.DicInit(pathMain)
        model.DelDic(dic)
    if number == 4:
        dic = model.DicInit(pathMain)
        model.ReinitData(dic)
    if number == 5:
        model.ConvertCsvToJson(pathMain, pathRes)
    if number == 6:
        file = input('Введите имя файла с расширением txt или csv: ')
        model.FileToFile(pathMain, file)
    if number == 7:
        viev.PrintBase()
    if number == 8:
        exit()





