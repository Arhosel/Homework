first = input('Введите первое число: ')
second = input('Введите второе число: ')
third = input('Введите третье число: ')
if first == second == third:
    print(3)
if first == second or second == third or first == third:          #= Равенство в Pyton
    print(2)
if first != second and second != third and first != third:        #!= Неравенство в Pyton
    print(0)
