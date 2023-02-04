from collections import defaultdict
def Print(massage):
    print(massage)

def PrintBase():
    with open('main.csv', 'r', encoding='utf-8') as file:
        data = file.read().split('\n')
        data = list(filter(None, data))
        for k, i in enumerate(data):
            i = i.split(';')
            temDic = {'name': i[0], 'status': i[1], 'salary': i[2]}
            Print(temDic)