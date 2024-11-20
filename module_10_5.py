import os
from multiprocessing import Pool
import time


def read_info(filename):
    all_data = []
    with open(filename, 'r') as file:                                                                                   #Открытие файла для чтения
        while True:
            line = file.readline()                                                                                      #Построчное считывание информации
            if not line:                                                                                                #Остановка при обнаружении пустой строки
                break
            all_data.append(line.strip())                                                                               #Добавление результата в конец списка

def main():
    filenames = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

    # Линейное выполнение
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    end_time = time.time()
    linear_time = end_time - start_time
    print(f"Линейный вызов: {linear_time:.4f} секунд")

    # Многопроцессное выполнение
    with Pool() as pool:
        start_time = time.time()
        results = pool.map(read_info, filenames)
        end_time = time.time()
        parallel_time = end_time - start_time
        print(f"Многопроцессный вызов: {parallel_time:.4f} секунд")

if __name__ == "__main__":
    main()                                                                                                              #Вызов функции main с условием её выполнения без импорта в другой файл 
