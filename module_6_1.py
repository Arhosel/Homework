class Animal():

    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

    def eat(self, food):
        if food.edible:
            print(f'{self.name}, съел {food.name}')             #Функция eat будет общей для всех подклассов,
            self.fed = True                                     #наследующих характеристики Animal
        else:
            print(f'{self.name}, не стал есть {food.name}')
            self.alive = False

class Plant():

    def __init__(self, name):
        self.name = name
        self.edible = False

                                                                #Определение классов, наследующих характеристики Animal
class Mammal(Animal):
    pass

class Predator(Animal):
    pass

                                                                #Определение классов, наследующих характеристики Plant
class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True

#Исходный код задания и проверка методов

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.
