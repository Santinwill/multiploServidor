import requests
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.testclient import TestClient

app = FastAPI()

jogadores = [
    {
        "id": 1,
        "nome": "Felipe",
        "time": "Santos",
        "idade": "19"
    },
    {
        "id": 2,
        "nome": "Carlos",
        "time": "Gremio",
        "idade": "38"
    },
    {
        "id": 3,
        "nome": "Maicon",
        "time": "Chapecoense",
        "idade": "33"
    }
]

rodas = [
    {
        "aro": 13,
        "cor": "Cromado"
    },
    {
        "aro": 15,
        "cor": "Cinza"
    },
    {
        "aro": 17,
        "cor": "Preto"
    },
]

client = TestClient(app)

@app.get("/api/jogador/{jogador_id}")
async def get_jogador(jogador_id: int):
    return jogadores[jogador_id]

@app.get("/api/rodas")
async def get_rodas():
    return rodas

def test_read_main():
    response = client.get("/api/jogador/1")
    assert response.status_code == 200
    assert response.json() == jogadores[1]
    # {
    #     "id": 2,
    #     "nome": "Carlos",
    #     "time": "Gremio",
    #     "idade": "38"
    # }

def test_read_rodas():
    response = client.get("/api/rodas")
    assert response.status_code == 200
    assert response.json() == rodas
