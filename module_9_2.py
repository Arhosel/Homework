first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(x) for x in first_strings if len(x) > 5]                                                            #Вывод длины строк с условием, что она не менее 5 символов

second_result = [(x,y) for x in first_strings for y in second_strings if len(x) == len(y)]                              #Вывод пар слов одинаковой длины из 2-х списков

third_result =  {x: len(x) for x in first_strings + second_strings if not len(x) % 2}                                   #Словарь с длиной строки и значением, вывод только чётных

print(first_result)
print(second_result)
print(third_result)
