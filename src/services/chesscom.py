from aiohttp import ClientSession
from fastapi import HTTPException, status


class ChessComApiService(object):
    async def get_games(self, player_name: str, year: int, month: int, session: ClientSession) -> list[str]:
        async with session.get(f'https://api.chess.com/pub/player/{player_name}/games/{year}/{month:02x}') as response:
            decoded = await response.json()
            return [game['pgn'] for game in decoded['games']]

    async def get_player_stats(self, player_name: str, session: ClientSession) -> dict[str]:
        async with session.get(f'https://api.chess.com/pub/player/{player_name}/stats') as response:
            if response.status != status.HTTP_200_OK:
                raise HTTPException(status_code=response.status)

            decoded = await response.json()
            tactics = decoded['tactics']['highest']['rating'] if 'tactics' in decoded else None
            rapid = decoded['chess_rapid']['last']['rating'] if 'chess_rapid' in decoded else None
            blitz = decoded['chess_blitz']['last']['rating'] if 'chess_blitz' in decoded else None
            bullet = decoded['chess_bullet']['last']['rating'] if 'chess_bullet' in decoded else None

            return {
                'tactics': tactics,
                'rapid': rapid,
                'blitz': blitz,
                'bullet': bullet,
            }
