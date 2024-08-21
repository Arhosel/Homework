immutable_var = (1, 2, 3, 4, True, 'String')
print('immutable tuple:', immutable_var)
#tuple[1][0] = 10       #обращение к конкретным элементам внутри кортежа не поддерживается
mutable_list = ['1, 2, 3, 4'[::-1], False, 'Not String']
mutable_list[-1] = 'Modified'      #Замена Not String-последнего элемента кортежа на Modify
print("Mutable List:", mutable_list)
mutable_list2 = ['1, 2, 3, 4'[::-1], False, 'Not String']
mutable_list2[1] = True      #Замена False на True
print("Mutable List2:", mutable_list2)
