import asyncio
from concurrent.futures import ProcessPoolExecutor

def encrypt(data):
    return f" {data[: : -1]}"



async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor(max_workers=10) as executor:
        result = await loop.run_in_executor(
            executor,
            encrypt,
            "card_no_2468",
        )
        print(f"{result}")

asyncio.run(main())
