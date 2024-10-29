first = ['Strings', 'Student', 'Computers']                                                                             #2 списка из задания
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))                                     #Расчёт разницы длины строки у элементов списков
                                                                                                                        #если длины не равны

second_result = ((len(first[x]) == len(second[x])) for x in range(len(first)))                                          #Сравнение длины строки в одинаковых позициях

print(list(first_result))
print(list(second_result))                                                                                              #Вывод результатов расчёта переменных
