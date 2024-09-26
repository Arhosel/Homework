def calculate_structure_sum(data_structure):
    summa = 0                                                       #Создание фнукци подсчёта данных строк и чисел
    if isinstance(data_structure, dict):
        for key, value in data_structure.items():
            summa += calculate_structure_sum(key)                   #Прописываем условие при помощи цикла 1 summa для key и value
            summa += calculate_structure_sum(value)
    elif isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            summa += calculate_structure_sum(item)                  #цикл 2 добавление к сумме - списка,кортэжа,множества
    elif isinstance(data_structure, (int, float)):
        summa += data_structure                                     #добавление целого числа и числа с плавающей запятой
    elif isinstance(data_structure, str):
        summa += len(data_structure)                                #добавление ключей через len
    return summa                                                    #возврат значения summa после выполнения функции

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),                                      #Исходные данные из задания
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)                                                       #Вывод результата
