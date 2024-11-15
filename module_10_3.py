import time
import random
import threading
from threading import Lock

class Bank:

    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = Lock()


    def deposit(self):
        for i in range(100):                                                                                            #метод совершает 100 транзакций пополнения средств
            if self.balance >= 500 and self.lock.locked():                                                              #разблокировка методом release при балансе > 500
                self.lock.release()
            random_int = random.randint(50, 500)                                                                  #случайное пополнение на число от 50 до 500
            self.balance += random_int
            print(f'Пополнение: {random_int}. Баланс: {self.balance}')                                                  #вывод строки результата пополнения
            time.sleep(0.1)                                                                                           #ожидание в 0.001 секунды-имитация скорости выполнения


    def take(self):
        for i in range(100):                                                                                            #метод совершает 100 транзакций снятия
            random_int = random.randint(50, 500)
            print(f'Запрос на {random_int}.')                                                                           #сообщение о снятии в начале
            if random_int <= self.balance:
                self.balance -= random_int                                                                              #проверка на возможность успешного снятия
                print(f'Снятие: {random_int}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()                                                                                     #Отклонение запроса о снятии в случаи превышения
                time.sleep(0.1)


bk = Bank()
                                                                                                                        #Исходный код из задания
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
