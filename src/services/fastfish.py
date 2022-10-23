import secrets

import aiohttp
from fastapi import HTTPException, status
from settings import settings


class FastfishApiService(object):
    fastfish_url = settings.fastfish_url

    async def get_analysis(self, games: list[str], player_name: str) -> dict[str]:
        payload = {
            'pgn': secrets.choice(games),
            'user': player_name,
        }
        headers = {'X-API-KEY': settings.fastfish_api_key}
        async with aiohttp.ClientSession(headers=headers) as s:
            async with s.post(f'{self.fastfish_url}/stockfish/analyze/', json=payload) as response:
                analysis = await response.json()

                if response.status != status.HTTP_200_OK:
                    raise HTTPException(status_code=response.status)

                return analysis
