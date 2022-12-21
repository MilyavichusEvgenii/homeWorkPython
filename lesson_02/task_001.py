#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
#- 6782 -> 23
#- 0,56 -> 11
import re
def TryNumb():
        listNum = []
        value = input("Введите целое число, или дробное число отделяя целую и дробную часть знаком ',': ")
        listNum = re.split("|,|0|-", value)
        data = list(filter(None, listNum))
        result = [int(item) for item in data]
        return (result, value)

def RecSum(a, b):
    count = 0
    if b == len(a):
        return count
    else:
        count+=a[b]
        return RecSum(a, b + 1) + count

(listNumber, strNumb) = TryNumb()
number = RecSum(listNumber, 0)
print(f'Сумма коэффициентов разрядов числа {strNumb} равна {number}')