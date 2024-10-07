class Vehicle:
    __COLOR_VARIANTS = ['black', 'white', 'blue', 'red', 'green']      #Атрибуты класса (цвета)
    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner                                             #Атрибуты объекта
        self.__model = __model
        self.__color = __color
        self.__engine_power = __engine_power

    def get_model(self):
        return f'Модель: {self.__model}'                               #Метод get_model - Возвращает название модели

    def get_color(self):
        return f'Цвет авто: {self.__color}'                            #Метод get_color - Возвращает цвет авто

    def get_horsepower(self):
        return f'Мощность двигателя в Л/С: {self.__engine_power}'      #Метод get_horsepower - Возвращает мощность движка

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())                                   #Метод print_info - Выводит результаты методов
        print(self.get_color())
        print(f'Владелец Т/С: {self.owner}')

    def set_color(self, new_color: str):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color                                   #Метод set_color - Принимает аргумент new_color(str)
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5                                             #Установка лимита пассажиров для седана

#Исходный код задания и проверка методов

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II',
                 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
