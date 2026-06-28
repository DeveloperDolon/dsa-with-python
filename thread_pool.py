import asyncio;
import time;
from concurrent.futures import ThreadPoolExecutor;

def check_stock(item):
    print(f'Checking {item} in store...');
    time.sleep(2);
    print(f'{item} stock: 42');

# async def main():
#     loop = asyncio.get_running_loop();

#     with ThreadPoolExecutor() as pool:
#         result = await loop.run_in_executor(pool, check_stock, "Masala Chai");
#         print(result);

# asyncio.run(main());

def side_task():
    print("  [side_task] Started!")
    time.sleep(0.5)
    print("  [side_task] Running at 0.5s...")
    time.sleep(0.5)
    print("  [side_task] Running at 1.0s...")
    time.sleep(0.5)
    print("  [side_task] Running at 1.5s...")
    time.sleep(0.5)
    print("  [side_task] Done at 2.0s!")

async def main():
    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor() as pool:
        await asyncio.gather(
            loop.run_in_executor(pool, check_stock, "Masala Chai"),
            loop.run_in_executor(pool, side_task, )
        )

    print("\nBoth done!")

asyncio.run(main())