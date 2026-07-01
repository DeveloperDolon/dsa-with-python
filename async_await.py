import asyncio;
import aiohttp;

async def fetch_url(session, url):
    async with session.get(url) as response: 
        print(f'Fetched url {url} with status {response}');

async def main():
    urls = ['https://jsonplaceholder.typicode.com/posts'] * 3;
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls];
        await asyncio.gather(*tasks);

asyncio.run(main());
