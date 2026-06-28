
import asyncio;
import time;
from concurrent.futures import ProcessPoolExecutor;
import threading;

def encrypt(data):
    return f"🔒{data[::-1]}";

async def main():
    loop = asyncio.get_running_loop();

    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, encrypt, "Dolon_roy");
        print(f'Data encrypted: {result}');


# making a logger 
def logging():
    while True:
        time.sleep(1);
        print(f"System health check🧑‍⚕️");


async def fetch_url():
    time.sleep(3);
    print('Data retrieved from url!');

threading.Thread(target=logging, daemon=True).start();

asyncio.run(fetch_url());

# if __name__ == '__main__':
#     asyncio.run(main());
