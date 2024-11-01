class StepValueError(ValueError):
    pass                                                                                                                #Создание класса исключения

class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start                                                                                              #start - целое число с которого начинается итерация
        self.stop = stop                                                                                                #stop - целое число на котором заканчивается итерация
        self.step = step                                                                                                #step - шаг с которой совершается итерация
        self.pointer = start                                                                                            #pointer - указывает на текущее число в итерации (start-начальное значение)
        if step == 0:                                                                                                   #проверка step для вывода ошибок
            raise StepValueError('Шаг не может быть равен 0')

    def __iter__(self):
        self.pointer = self.start                                                                                       #метод сбрасывающий значение pointer
        return self                                                                                                     #на start и возвращающий сам объект итератора

    def __next__(self):
        current_element = self.pointer                                                                                  #метод увеличивающий атрибут pointer на step
        self.pointer += self.step
        if self.step > 0 and current_element > self.stop or self.step < 0 and current_element < self.stop:
            raise StopIteration()

        return current_element

#Пример выполняемого кода из задания
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()
