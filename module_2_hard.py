def pairs(rand_number):
    pairs_numb = list()                                         #добавление списка
    limit_first_numb = (rand_number + 1) // 2
    for i in range(1, limit_first_numb):                        #Первый цикл For
        j = i + 1
        while i + j <= rand_number:                             #Вложенный цикл While
            if rand_number % (i + j) == 0:                      #проверка на остаток от деления
                tuple_numbers = (i, j)
                pairs_numb.append(tuple_numbers)
            j += 1                                              #увеличение индекса
    return pairs_numb


fn = True
while fn:
    result = int(input('Введите число из первого поля: '))
    if result in range(3, 21):                                  #Установка возможного диапазона значений переменной
        fn = False
    else:
        print('Введено число за пределами интервала [3, 20]')
        print('Повторите ввод')
print(*pairs(result), sep='')                                   #Вывод результата с распаковкой списка
