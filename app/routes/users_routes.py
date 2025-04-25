from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from app.schemas.response_schema import SuccessResponseSchema

# Services
from app.services.user_services import UserService

# DB
from app.db.db_config import get_db

# Schemas
from app.schemas.user_schemas import UserCreate, UserResponse


router = APIRouter(
    prefix="/users", 
    tags=["users"]
)


@router.post('/',response_model=SuccessResponseSchema, status_code=status.HTTP_201_CREATED)
def criar_usuario(user:UserCreate, db: Session = Depends(get_db)):
    """
        Rota para criar um novo usuário
    """

    new_user =   UserService.create_new_user(user, db)


    res =  SuccessResponseSchema(
        status=status.HTTP_201_CREATED,
        message="Usuário criado com sucesso",
        data=UserResponse.model_validate(new_user)
    )

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=res.model_dump()
    )


@router.get('/', response_model=SuccessResponseSchema, status_code=status.HTTP_200_OK)
def get_all_users(db: Session = Depends(get_db)):
    """"
        Rota para obter todos os usuarios
    """