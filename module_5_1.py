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

h1 = House('ЖК Горский', 18)                                #Исходный код из задания
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
