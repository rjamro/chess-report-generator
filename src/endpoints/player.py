from fastapi import APIRouter, Depends, Path
from aiohttp import ClientSession
from dependencies.session import get_session
from models.player import PlayerResponse
from services.chesscom import ChessComApiService

router = APIRouter(prefix='/players', tags=['players'])


@router.get('/{player_name}/')
async def get_player(
    player_name: str = Path(title="The player name"),
    session: ClientSession  = Depends(get_session),
):
    api_service = ChessComApiService()
    stats = await api_service.get_player_stats(player_name=player_name, session=session)

    return PlayerResponse(**stats)
