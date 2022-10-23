from pydantic import BaseSettings, Field, validator


class Settings(BaseSettings):
    fastfish_url: str = Field(default='http://fastfish:8000')
    chesscom_url: str = Field(default='https://api.chess.com')

    fastfish_api_key: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
