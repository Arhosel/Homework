def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()                        #Вызов функции Inner внутри Test

test_function()                             #Вызов функции Test
#inner_function()                           #NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
                                            #Любезно прокомментированная Pycharm попытка вызвать Inner в глобальном пространстве
