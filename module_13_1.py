import time
import asyncio


async def start_strongman(name, power):
    """

    :param name: - имя силача
    :param power: - его сила
    :return:
    """
    print(f"Силач {name} начал соревнования.")
    for i in range(1, 6):
        person_power = power
        print(f"Силач {name} поднял {i} шар.")
        await asyncio.sleep(power)
        person_power -= i
    print(f"Силач {name} закончил соревнования")


async def start_tournament():
    task_1 = asyncio.create_task(start_strongman('Pasha', 3))
    task_2 = asyncio.create_task(start_strongman('Denis', 4))
    task_3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task_1
    await task_2
    await task_3


start = time.time()
asyncio.run(start_tournament())
finish = time.time()

print(f"Runtime {round(finish - start, 3)}")