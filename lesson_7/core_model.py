#Задание в группах: Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.

from collections import defaultdict
def Core():
    while True:
        name = input('Введите имя: ')
        tel = int(input('Введите номер телефона: '))
        with open('base.csv', 'a', encoding='utf-8') as file:
            file.write('name: {}; tel: {}\n'
                        .format(name, tel))
        if int(input('Если вы хотите продолжать операцию, нажмите 1, в противном случае 0: ')) == 0:
            break
     

    