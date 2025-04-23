from fastapi import FastAPI, Depends, HTTPException
from fastapi.exceptions import RequestValidationError

from sqlalchemy.orm import Session
from sqlalchemy import text 


from app.db.db_config import get_db, Base, engine
from app.routes import users_routes

from app.exceptions.exceptions_handler import ExceptionHandler

app = FastAPI()
# criação das tabelas
Base.metadata.create_all(bind=engine)

# Exceptions handler
app.add_exception_handler(RequestValidationError, ExceptionHandler.request_validation_error)
app.add_exception_handler(HTTPException, ExceptionHandler.http_exceptions)

# Rotas
app.include_router(users_routes.router)




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

