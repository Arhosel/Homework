numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []                                                     # Будущий список простых чисел
not_primes = []                                                 # Будущий список сложных чисел
index = 0                                                       # Ввод переменной для отсчёта

for index in numbers:
    if index == 1:                                              # Сравниваем значение переменной с единицей
        continue
    is_prime = True                                             # Переменная - флаг
    for i in range(2, index):                                   # Функция Range возвращает последовательность в 2 аргумента
                                                                # Здесь задаём значение этой последовательности
        if index % i == 0:
            is_prime = False                                    # Проверка на остаток от деления
            break
    if is_prime:
        primes.append(index)                                    # При срабатывании флага значение записывается в список Primes
    else:
        not_primes.append(index)                                # В обратном случае, значение попадает в список Not Primes

print("Исходный список: ", numbers)
print("Primes: ", primes)
print("Not Primes: ", not_primes)
