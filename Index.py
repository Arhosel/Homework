a = 'Топинамбур'
print(a[0])
print(a[-1])
print(a[5:])                    #вывод части строки по количеству символов
print(a[::-1])                  #вывод слова наоборот
print(a[1::2])                  #вывод каждого второго символа
first_half  = a[:len(a)//2]     #вариант вывода части строки через функцию len подсмотрел в сети
second_half = a[len(a)//2:]
print(second_half)


b = 'Ложь требует мысленных усилий. Это занимает время. ©Дрю Карпишин'
first_half  = b[:len(b)//2]
second_half = b[len(b)//2:]
print(first_half)
print(second_half)          #просто посмотрел как работает функция на более длинной строке :)
print(b[1::2])              #ну и вывод каждого второго символа
