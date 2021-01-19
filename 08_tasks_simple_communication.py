import asyncio


async def independent_task(queue: asyncio.Queue):
    """tento task je nezavisly na parentovi (neposila mu zadna data zpet, je to napriklad logovani)

    """
    print("starting the child")
    val = await queue.get()

    while val is not None:
        print("Received is %s and processing data" % str(val))
        await asyncio.sleep(0.5)  # procesovani zabere nejaky cas, aby se demonstrovala kapacita fronty
        print("Received data processed")
        queue.task_done()
        val = await queue.get()

    queue.task_done()  # oznacuje poslední None hodnotu, ktera ukoncila cyklus
    print("The client is done here")


async def parent_task(queue: asyncio.Queue):
    print("Starting the parent")
    for i in range(10):
        print("Sending value %d" % i)
        await queue.put(i)  # pokud je fronta plna, pak se ceka, az se uvolni misto
        await asyncio.sleep(0.1)

    await queue.put(None)
    await queue.join()
    print("Parent is done here")


async def main():
    queue = asyncio.Queue(maxsize=3)
    child = asyncio.create_task(independent_task(queue))
    parent = asyncio.create_task(parent_task(queue))

    await asyncio.gather(child, parent)


asyncio.run(main())
