def get_multiplied_digits(number):
    str_number = ( str(number) )                                        #Создание переменной и запись строкового значения числа number
    first = int( str_number [0] )                                       #Преобразование в числовое при помощи int
    if len( str_number ) > 1:                                           #Постановка условия длина списка >1 для осуществления среза
        return first * get_multiplied_digits(int ( str_number[1:] ))
    else:
        return first

result = get_multiplied_digits(40203)                                   #Исходный код задания
print(result)
