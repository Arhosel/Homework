import os
import time
main_path = os.getcwd()
for root, dirs, files in os.walk('.'):
    root = root[2:]
    for file in files:
        if os.path.isfile(file):
            filepath = os.path.join(main_path, root, file)                                                              #Формирование полного пути к файлу
            filetime = os.path.getmtime(file)
            formatted_time = time.ctime(filetime)                                                                       #Получение времени последнего изменения файла
            filesize = os.stat(file).st_size                                                                            #Получение размера файла
            parent_dir = os.path.dirname(filepath)                                                                      #Получение родительской директории файла
            print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт,'
                  f' Время изменения: {formatted_time}, Родительская директория: {parent_dir}')                         #Вывод данных в консоль
