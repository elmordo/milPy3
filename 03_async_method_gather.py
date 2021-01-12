import asyncio
import random


async def get_random_number(msg):
    await asyncio.sleep(random.random() * 2)
    print(msg)
    return random.random()


async def main():
    vals = await asyncio.gather(get_random_number("foo"), get_random_number("bar"))
    return sum(vals)


result = asyncio.run(main())
print(result)
