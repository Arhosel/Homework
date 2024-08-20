my_string = str(input('Введите произвольную строку:'))
print(len(my_string))
print(my_string.lower())                           #Строка в нижнем регистре
print(my_string.upper())                           #Строка в верхнем регистре
print(my_string.replace(' ',''))      #old и new подтягиваются автоматически, прописывать вручную НЕ нужно (Замена разделителя)
print(my_string[0])                                #Вывод на экран первого символа строки
print(my_string[-1])                               #Вывод на экран последнего символа строки
