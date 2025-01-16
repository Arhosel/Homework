import asyncio

# Асинхронная функция для моделирования участия силача в соревнованиях
async def start_strongman(name: str, power: int):
    print(f'Силач {name} начал соревнования.')

    # Цикл, моделирующий поднятие 5 шаров
    for ball in range(1, 6):
        # Имитация времени, затрачиваемого на поднятие шара, зависящего от силы силача
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {ball} шар')

    print(f'Силач {name} закончил соревнования.')

# Асинхронная функция для запуска турнира силачей
async def start_tournament():
    # Создание задач для трёх участников с различной силой
    task1 = asyncio.create_task(start_strongman('Appollon', 5))  # Appollon с силой 5
    task2 = asyncio.create_task(start_strongman('Pasha', 3))    # Pasha с силой 3
    task3 = asyncio.create_task(start_strongman('Denis', 4))     # Denis с силой 4

    # Ожидание завершения всех задач
    await task1
    await task2
    await task3

# Запуск турнира
asyncio.run(start_tournament())
