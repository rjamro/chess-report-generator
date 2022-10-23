import aiohttp


async def get_session() -> aiohttp.ClientSession:
    async with aiohttp.ClientSession() as session:
        yield session
