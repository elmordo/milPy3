import asyncio


def normal_fn():
    return 1


async def async_fn():
    return 5


async def main():
    return normal_fn() + await async_fn()


coro = main()  # volani vytvori coroutine
print(coro)
result = asyncio.run(coro)
print(result)
