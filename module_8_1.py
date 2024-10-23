def add_everything_up(a, b):
    try:
        summ = a + b                                #Сумма параметров
        return round(summ, 3)                       
    except TypeError:
        return f'{a}{b}'                            #возврат f строки при попытке сложения строки и числа 

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
