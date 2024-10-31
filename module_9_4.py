from random import choice

#Lambda-функция:
first = 'Мама мыла раму'
second = 'Рамена мало было'
res = list(map(lambda x, y: x == y, first, second))
print(res)

#Замыкание:
def get_advanced_writer(file_name):
    def write_everything(*data_set):                                                                                    #data_set - параметр принимающий неограниченное
        with open(file_name, mode='w', encoding='utf-8') as file:                                                       #количество данных любого типа
            for i in data_set:                                                                                          #добавление в файл file_name всех данных 
                file.write(f"{i}\n")                                                                                    #из data_set в том же виде
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

#Метод __call__:
class MysticBall:
    def __init__(self, *words: str):                                                                                    #класс MysticBall, объекты которого обладают
        self.words = words                                                                                              #атрибутом words хранящий коллекцию строк

    def __call__(self):                                                                                                 #метод __call__ который будет случайным образом
        return choice(self.words)                                                                                       #выбирать слово из words и возвращать его

#Исходный код из задания
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
