from aiohttp import ClientSession
from fastapi import APIRouter, Depends, Path

from dependencies.session import get_session
from models.errors import NotFound
from models.player import PlayerResponse
from services.chesscom import ChessComApiService

router = APIRouter(prefix='/players', tags=['players'])


@router.get(
    path='/{player_name}/',
    response_model=PlayerResponse,
    responses={404: {'model': NotFound, 'description': 'Player does not exist.'}},
)
async def get_player(
    player_name: str = Path(title="The player name"),
    session: ClientSession = Depends(get_session),
):
    api_service = ChessComApiService()
    stats = await api_service.get_player_stats(player_name=player_name, session=session)

    return PlayerResponse(**stats)
