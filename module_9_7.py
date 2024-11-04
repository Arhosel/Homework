def is_prime(func):
    def wrapper(*args):                                                                                                 #Функция декоратор (is_prime)
        result = func(*args)                                                                                            #распечатывает "Простое", если результат - простое число
        k = 0                                                                                                           #"Составное" в противном случае
        for i in range(1, result+1):
            if result % i == 0:                                                                                         #Функция range позволяет перебрать результаты
                k += 1                                                                                                  #выполнения функции и определить тип числа
        if k == 2:
            print('Простое число')
        else:
            print('Составное число')
        return result
    return wrapper


@is_prime
def sum_three(a, b, c):                                                                                                 #Функция, которая складывает 3 числа
    return a+b+c

#Пример выполняемого кода из задания
result = sum_three(2, 3, 6)
print(result)
