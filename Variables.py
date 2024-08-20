home_work = 12              #Количество выполненных ДЗ
hours_spent = 1.5           #Количество затраченных часов
course_name = 'Pyton'       #Название курса
time_for_one_task = (hours_spent/home_work)     #Время затраченное на одно задание

print('Курс:',course_name, 'Всего задач:', home_work, 'Затрачено часов:', hours_spent, 'Среднее время выполнения:', time_for_one_task, 'часа', sep=' ')
print('Курс:',str(course_name),'Всего задач:',str(home_work),'Затрачено часов:',str(hours_spent), 'Среднее время выполнения:', str(time_for_one_task), 'часа', sep=',')
