import asyncio
import random


async def task(i):
    await asyncio.sleep(random.random())
    print("task finished: %d" % i)


async def main():
    tasks = []
    for i in range(3):
        my_task = asyncio.create_task(task(i))  # je to spatne, ale tady to projde
        tasks.append(my_task)
    for i in range(3, 6):
        my_task = asyncio.create_task(task(i))  # a tady se to posere
        tasks.append(my_task)

    await asyncio.gather(*tasks)


asyncio.run(main())
