import asyncio
import random


async def random_numbers(n: int) -> float:
    for i in range(n):
        print(i)
        await asyncio.sleep(1)
        yield random.random()


async def main():
    total = 0

    async for x in random_numbers(5):
        print(x)
        total += x

    return total


x = asyncio.run(main())
print(x)
