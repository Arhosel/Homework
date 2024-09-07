def single_root_words(root_word, *other_words):
    same_words = []
    root_word_lower = root_word.lower()                                #исключаем влияние регистра переводя всё в нижний
    for i in other_words:
        other_words_lower = i.lower()
        if (root_word_lower in other_words_lower                       #проверка наличия слова в составе другого из списка
                or other_words_lower in root_word_lower):
            same_words.append(i)                                       #добавление прошедшего проверку значения в список вывода
    return same_words


result1 = single_root_words('rich', 'richiest',    #исходный код для проверки работы функции из задания
                            'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able',
                            'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
