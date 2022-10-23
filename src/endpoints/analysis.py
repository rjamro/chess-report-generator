from datetime import datetime

from aiohttp import ClientSession
from fastapi import APIRouter, Depends, Path, Query

from dependencies.session import get_session
from models.analysis import GameAnalysis
from models.errors import NotFound
from services.chesscom import ChessComApiService
from services.fastfish import FastfishApiService

router = APIRouter(prefix='/analysis', tags=['analysis'])


@router.get(
    path='/{player_name}/',
    response_model=GameAnalysis,
    responses={404: {'model': NotFound, 'description': 'Player does not exist.'}},
)
async def get_stats(
    player_name: str = Path(title='The player name', max_length=100),
    month: int | None = Query(default=None, title='The month to analyze', ge=1, le=12),
    year: int | None = Query(default=None, title='The year to analyze', ge=2000, le=9999),
    session: ClientSession = Depends(get_session),
):
    now = datetime.now()

    chesscom_api_service = ChessComApiService()
    games = await chesscom_api_service.get_games(
        player_name=player_name,
        year=year or now.year,
        month=month or max(1, now.month - 1),
        session=session,
    )

    fastfish_api_service = FastfishApiService()
    analysis = await fastfish_api_service.get_analysis(
        games=games,
        player_name=player_name,
    )

    return GameAnalysis(**analysis)
