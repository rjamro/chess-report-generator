from fastapi import FastAPI

from endpoints import analysis, player

app = FastAPI(
    title='ChessReport',
    description=(
        'The ChessReport is a web server, that provides general information'
        ' about players and analysis of their games.'
    ),
)
app.include_router(player.router)
app.include_router(analysis.router)


@app.get('/')
async def root():
    return {
        'message': 'Welcome to ChessReport API, a web server providing excellent insights into your game!'
    }
