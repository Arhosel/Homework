calls = 0                                                               #Создание глобальной переменной с изменяемым значением

def count ():                                                           #Объявляем функции count, string_info и is_contains
    global calls
    calls += 1
def string_info (string):
    count()                                                              #добавляем параметр string
    return (len(string), string.upper(), string.lower())                 #возвращаем длину списка, в дальнейшем выводим отдельные элементы в нужном регистре
def is_contains (string, list_to_search):
    count()                                                              #добавляем параметры string и list_to_search
    return string.upper() in [s.upper() for s in list_to_search]         #проверка на наличие строки в списке

print(string_info('Capybara'))                                           #Пример выполняемого кода из задания
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)                                                             #Возврат в консоль итогового значения переменной calls(обращения к функции)
