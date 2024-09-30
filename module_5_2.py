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

h1 = House('ЖК Эльбрус', 10)             #Исходный код из задания
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
