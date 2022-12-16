# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# (расшифровка этого выражения not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2]) для всех значений предикат.

print('Тааблица истинности утверждения ¬(X V Y V Z) = ¬X ⋀ ¬Y ⋀ ¬Z:')
for i in True, False:
    for j in True, False:
        for k in True, False:
            if not(i or j or k) == (not i and not j and not k):
                print(f"не ({i} или {j} или {k}) = не {i} и не {j} и не {k} будет истинным данное утверждение")
            else:
                print(f"не ({i} или {j} или {k}) = не {i} и не {j} и не {k} будет ложным данное утверждение")




