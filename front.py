import requests
import json
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/jogador/{jogador_id}", response_class=HTMLResponse)
async def get_jogador(jogador_id: int):
    print(f"http://127.0.0.1:8000/api/{jogador_id}")
    jogador = json.loads(requests.get(f"http://127.0.0.1:8000/api/jogador/{jogador_id}").content)
    print(jogador)

    return f"""
    <html>
        <head>
            <title>Jogador</title>
        </head>
        <body>
            <ul>
                <li>{jogador['nome']}</li>
            </ul>
        </body>
    </html>
    """
