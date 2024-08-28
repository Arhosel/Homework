def get_matrix(n, m, vaule):
    matrix = []                                     #после объявления функции и ввода параметров создаём пустой список
    for i in range(n):                              #создаём внешний цикл for для ввода количества строк с n повторений
        row =[]
        for g in range(m):                          #создаём внешний цикл for для количества столбцов матрицы с m повторений
           row.append(vaule)
        matrix.append(row)
    return matrix                                   #возврат значения переменной matrix после выполнения всех циклов

result1 = get_matrix(2, 2, 10)                      #исходный код задачи со значениями переменных
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)
