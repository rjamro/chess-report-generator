from pydantic import BaseModel


class GameAnalysis(BaseModel):
    blunders: int
    total_moves: int
