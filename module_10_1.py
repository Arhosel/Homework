from time import sleep
from threading import Thread
from datetime import datetime


def wite_words(word_count, file_name):
    for i in range(1, word_count + 1):
        with open(file_name, 'a', encoding="utf-8") as file:
            file.write(f'Какое-то слово № {i}\n')                                                                       #Функция, которая ведёт запись слов в соответсвующий файл
            sleep(0.1)                                                                                                  #интервал прерывания после записи каждого слова
    file.close()
    print(f'Завершилась запись в файл {file_name}')

time_start1 = datetime.now()                                                                                            #Вызов функции write_worlds с установкой точки отсчёта времени на текущее
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')                                                                                          #Запуск функций с аргументами из задачи
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
time_end1 = datetime.now()                                                                                              #Взятие текущего времени
time_res1 = time_end1 - time_start1
print(time_res1)                                                                                                        #Вывод разницы начала и конца работы функций

time_start2 = datetime.now()                                                                                            
the_f1 = Thread(target=wite_words, args=(10, "example5.txt"))
the_f2 = Thread(target=wite_words, args=(30, "example6.txt"))
the_f3 = Thread(target=wite_words, args=(200, "example7.txt"))
the_f4 = Thread(target=wite_words, args=(100, "example8.txt"))

the_f1.start()
the_f2.start()                                                                                                          #Создание и запуск потоков с аргументами из задачи
the_f3.start()
the_f4.start()

the_f1.join()
the_f2.join()
the_f3.join()
the_f4.join()
time_end2 = datetime.now()
time_res2 = time_end2 - time_start2                                                                                     #Вывод разницы начала и конца работы потоков
print(time_res2)
