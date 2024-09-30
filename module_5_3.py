class House:
    def __init__(self, name, number_of_floors):
        self.name = name                                    #Создание класса и объявление метода и атрибутов
        self.number_of_floors =  number_of_floors

    def go_to(self, new_floor):
        for i in range(1, new_floor + 1):
            if 1 <= new_floor <= self.number_of_floors:     #Условие по которому будут проходиться этажи
                print(i)                                    #Вывод каждого пройденного параметра
            else:
                print('Такого этажа не существует')         #Остановка в случае превышения лимита
                break
    def __str__(self):
        return f'Название ЖК: {self.name}, количество этажей: {self.number_of_floors}'
#Метод, возвращащий F строку с нужными параметрами
    def __len__(self):
        return self.number_of_floors
#Метод, возвращающий количество этажей здания
    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __radd__(self, value):
        self.number_of_floors += value
        return self

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors
#Различные методы, по которым будет проводиться проверка

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

#Пример выполняемого кода из задания
print(h1)
print(h2)

print(h1 == h2)                                             # __eq__

h1 = h1 + 10                                                # __add__
print(h1)
print(h1 == h2)

h1 += 10                                                    # __iadd__
print(h1)

h2 = 10 + h2                                                # __radd__
print(h2)

print(h1 > h2)                                              # __gt__
print(h1 >= h2)                                             # __ge__
print(h1 < h2)                                              # __lt__
print(h1 <= h2)                                             # __le__
print(h1 != h2)                                             # __ne__
