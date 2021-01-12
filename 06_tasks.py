import asyncio
import random


async def task(i):
    await asyncio.sleep(random.random())
    print("task finished: %d" % i)


async def main():
    tasks = []
    for i in range(3):
        my_task = asyncio.create_task(task(i))
        tasks.append(my_task)

    for t in asyncio.Task.all_tasks():
        await my_task

    await asyncio.gather(*tasks)


asyncio.get_event_loop().run_until_complete(main())
