class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model                                                                                              #Вызов методов для создания атрибутов объекта
        if self.__is_valid_vin(vin):
            self.__vin = vin                                                                                            #модели, VIN номера и строчного номера авто
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers

    def __is_valid_vin(self, vin_number):
                                                                                                                        #Выбрасывает исключение IncorrectVinNumber
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber("Некорректный тип vin номер")                                                      #если передано не целое число
        if not (1000000 <= vin_number <= 9999999):                                                                      
            raise IncorrectVinNumber("Неверный диапазон для vin номера")                                                #если переданное число находится не в диапазоне
        else:
            return True

    def __is_valid_numbers(self, numbers):
                                                                                                                        #Выбрасывает исключение IncorrectCarNumbers
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")                                            #если передана не строка
        if len(numbers) != 6:
            raise IncorrectCarNumbers("Неверная длина номера")                                                          #если переданная строка не состоит ровно из 6 символов
        else:
            return True                                                                                                 #True, если исключения не были выброшены

#Пример выполняемого кода из задания
try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
