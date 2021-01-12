import asyncio
import random


async def synced_task(name, cycles: int, shared_lock: asyncio.Lock):

    for i in range(cycles):
        print("%s - jdu charapt" % name)
        await asyncio.sleep(random.random() * 2)
        print("%s - cekam na lock" % name)
        await shared_lock.acquire()
        print("%s - mam lock a makam" % name)
        await asyncio.sleep(random.random() * 2)
        print("%s - hotovo, vracim lock" % name)
        shared_lock.release()
        print("%s - lock vracen" % name)

    print("Hotovo, mrdam na to, jdu domu, zasarana prace.")


async def main():
    tasks = []
    lock = asyncio.Lock()

    for i in range(3):
        name = "dric %d" % i
        t = asyncio.create_task(synced_task(name, 4, lock))
        tasks.append(t)

    await asyncio.gather(*tasks)


asyncio.run(main())
