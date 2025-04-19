from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text 

from app.db.db_config import get_db

app = FastAPI()


@app.get('/')
def infos_api(db : Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {
            "title": "Bem-vindo a API de Gerenciamento de tarefas",
            "status_db": "Conectado pronto para operar."

        }
    except Exception as e:
        return {
            "title": "Bem-vindo a API de Gerenciamento de tarefas",
            "status_db": "Erro ao conectar ao banco de dados.",
            "error": str(e)
            }  

