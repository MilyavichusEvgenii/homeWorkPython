#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = "Ах, не говорите мне про Австрию! Я ничего не понимаю, может быть, но Австрия никогда не хотела и не хочет войны. Она предает нас."
listStr = text.split()
resList = [listStr.pop(i) for i, r in enumerate(listStr) 
if r.lower().count("а") == False and r.lower().count("б") == False and r.lower().count("в") == False]
print(f"Изначальный текст: {text}")
print("Обработанный текст без слов, содержащих буквы а, б, в: ")
print(*resList)