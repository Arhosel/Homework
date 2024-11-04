def all_variants(text):
    x = 0                                                                                                               #функция-генератор 
    y = 0                                                                                                               #принимает строку text и возвращает объект-генератор
    for x in range(len(text)):
        for y in range(x+1, len(text)+1):
            yield text[x:y]


#Пример выполняемого кода из задания
z = all_variants("abc")
for i in z:
    print(i)
