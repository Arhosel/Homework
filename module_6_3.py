class Horse:
    def __init__(self):
        self.x_distance = 0                             # Пройденный путь
        self.sound = 'Frrr'                             # Звук, который лошадь издаёт
        super().__init__()                              # Метод super для дистанции

    def run(self, dx):
        self.x_distance += dx

class Eagle:
    def __init__(self):
        self.y_distance = 0                             # Ввод высоты и звука орла
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy                           # Метод, где dy - изменение дистанции, увеличивает высоту на dy

class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()

    def move(self, dx, dy):
        self.run(dx)                                    # Метод, где dx и dy изменения дистанции, запускает
        self.fly(dy)                                    # наследованные методы run и fly соответственно.

    def get_pos(self):
        return self.x_distance, self.y_distance         # Метод возвращает текущее положение в виде кортежа

    def voice(self):
        print(self.sound)                               # Звук пегаса

#Исходный код задания и проверка методов
p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
