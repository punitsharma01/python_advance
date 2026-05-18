import asyncio
import time

async def brew_coffee(name):
    print(f'Brewing ...{name}')
    await asyncio.sleep(3)
    # time.sleep(3)
    print(f'Coffee ready! # {name}')

async def main():
    await asyncio.gather(
        brew_coffee("Latte"),
        brew_coffee("Espresso"),
        brew_coffee("Classic"),
    )

asyncio.run(main())