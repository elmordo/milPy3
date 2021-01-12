import asyncio
import random


async def get_random_number():
    return random.random()


async def main():
    vals = await asyncio.gather(get_random_number(), get_random_number())
    return sum(vals)


result = asyncio.run(main())
print(result)
