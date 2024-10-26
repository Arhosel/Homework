def apply_all_func(int_list:(int, float), *functions):
    result = {}                                                                                                         #Объявляем функцию и создаём пустой словарь
    for func in functions:
        result[str(func.__name__)] = func(int_list)                                                                     #Перебираем каждую функцию и записываем результат
    return result

#Пример работы кода из задания
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
