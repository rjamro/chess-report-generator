from pydantic import BaseModel


class PlayerResponse(BaseModel):
    tactics: int | None = None
    rapid: int | None = None
    blitz: int | None = None
    bullet: int | None = None
