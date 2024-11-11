from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name, power):                                                                                    #Класс Knight, содержащий два метода (__init__, run),
        super().__init__()                                                                                              #наследуемый от материнского класса Thread
        self.name = name                                                                                                #Атрибут name - имя рыцаря
        self.power = power                                                                                              #Атрибут power - сила рыцаря

    def run(self):
        enemies_power = 100                                                                                             #Рыцарь сражается, пока не победит всех врагов
        number_days = 0
        print(f'{self.name}, на нас напали!')                                                                           #Надпись при запуске потока
        for i in range(enemies_power):
            if enemies_power > 0:                                                                                       #Условие работы цикла - наличие врагов
                enemies_power -= self.power
                number_days += 1                                                                                        #Счётчик дней
                sleep(1)
                print(f'{self.name} сражается {number_days} день(дня)...,'
                      f' осталось {enemies_power} войнов. ')                                                             #Вывод ежедневного отчёта
                if enemies_power <= 0:
                    print(f'{self.name} одержал победу спустя {number_days} дней(дня)!')                                #Итоговое сообщение после победы

# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
# Вывод строки об окончании сражения
print(f'Все битвы закончились!')
