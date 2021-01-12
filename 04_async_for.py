import asyncio
import random


async def random_numbers(n: int) -> float:
    for _ in range(n):
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
