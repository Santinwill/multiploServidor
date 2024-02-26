Para subir ambos os servidores com comunicação é necessário instalar os pacotes:

```
pip install "fastapi"
pip install "uvicorn[standard]"
pip install requests
```

Depois, para subir os servidores rode (em terminais diferentes):

```
python -m uvicorn front:app --port 8001 --reload
```

E
```
python -m uvicorn endpoints:app --port 8000 --reload
```

Depois, para testar a comunicação entre no link http://127.0.0.1:8001/jogador/2 
