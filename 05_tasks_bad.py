import asyncio
import random


async def make_task_1(i):
    print("task finished: %d" % i)


async def make_task_2(i):
    await asyncio.sleep(random.random() * 5)
    print("task finished: %d" % i)


async def main():
    for i in range(3):
        my_task = asyncio.create_task(make_task_1(i))  # je to spatne, ale tady to projde
    for i in range(3):
        my_task = asyncio.create_task(make_task_2(i))  # a tady se to posere


asyncio.get_event_loop().run_until_complete(main())
