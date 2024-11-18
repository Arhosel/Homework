import threading
import random
import time
from queue import Queue

class Table:
    def __init__(self, number: int):
        self.number = number
        self.guest = None

class Guest(threading.Thread):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables)

    def guest_arrival(self, *guests):
        for guest in guests:                                                                                            #Метод принимает неограниченное количество гостей
            table = self.find_free_table()
            if table:
                table.guest = guest                                                                                     #Проверка на наличие гостя за столом
                guest.start()                                                                                           #Запуск потока гостя, и вывод стоки с номером стола
                print(f'{guest.name} сел(-а) за стол номер {table.number}')
            else:
                self.queue.put(guest)                                                                                   #В случае провала проверки гость помещается в очередь
                print(f'{guest.name} в очереди')                                                                        #Вывод информационного сообщения

    def discuss_guests(self):
        while not self.queue.empty() or self.any_guest_still_seated():
            for table in self.tables:                                                                                   #Метод имитирует процесс обслуживания гостей
                if table.guest and not table.guest.is_alive():                                                          #Применение метода is-alive для определения завершения потока
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None

                if not self.queue.empty() and table.guest is None:
                    next_guest = self.queue.get()                                                                       #Если в очереди есть гости, и один из столов освободился
                    table.guest = next_guest                                                                            #то к этому столу добавляется гость из очереди
                    next_guest.start()                                                                                  #запуск следующего потока гостя
                    print(f'{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')

    def find_free_table(self):
        for table in self.tables:                                                                                       #Проверка на наличие свободного стола
            if table.guest is None:
                return table
        return None

    def any_guest_still_seated(self):
        return any(table.guest is not None for table in self.tables)                                                    #Проверка наличия гостя за столом функцией any(наличие элемента)


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
