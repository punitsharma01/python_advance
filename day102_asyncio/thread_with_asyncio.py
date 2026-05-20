import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def check_stock(item):
    print(f"checking in store {item}")
    time.sleep(3)
    return f"{item} stock : 34"

async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor(max_workers=10) as executor:
        result = await loop.run_in_executor(
            executor,
            check_stock,
            "Espresso"
        )
    print(result)

asyncio.run(main())