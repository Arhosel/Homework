my_dict = {'Oleg': 1980, 'Alex': 1994, 'Ksenia': 2000}
print('Dict:', my_dict)
print(my_dict.get('Ksenia', 'Такого ключа нет'))        #Запрос по имеющемуся ключу
print(my_dict.get('Denis', 'Такого ключа нет'))         #Запрос по отсутствующему ключу
my_dict.update({'Alexandr': 1986,                       #Добавление новых пар в словарь
                'Vladimir': 1894})
#print(my_dict)                                         #Проверил вывод всего словаря
a = my_dict.pop('Alex')                                 #Удаление ключа 'Аlex', возвращает значение по команде print
print('Dict:', my_dict)                                 #Вывод итогового словаря -Alex, +Alexandr & +Vladimir

my_set = {1, 2, 3, 4, 5, 'Denis', 'Ksenia', False, 
          'Никогда не выпадает вторая оказия создать первое впечатление', 
          (1,2,3,4), 'Denis'}
print('Set', my_set)
my_set.update({'Valeria',
               6, 7, 'Словарь дополнен в полночь'})
print(my_set.remove('Denis'))
print('Final Set', my_set)
