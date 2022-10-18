import secrets

from aiohttp import ClientSession
from fastapi import HTTPException, status


class FastfishApiService(object):
    async def get_analysis(self, games: list[str], player_name: str, session: ClientSession) -> dict[str]:
        payload = {
            'pgn': secrets.choice(games),
            'user': player_name,
        }

        async with session.post('http://fastfish:8000/stockfish/analyze/', json=payload) as response:
            analysis = await response.json()

            if response.status != status.HTTP_200_OK:
                raise HTTPException(status_code=response.status)

            return analysis
