from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.db.db_config import get_db


from app.schemas.auth_schemas import AuthSchemas

from app.services.auth_services import AuthService


router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@router.post("/")
def login(login_data: AuthSchemas, db: Session = Depends(get_db)):
    """"
        Rota de login 
    """

    res = AuthService.login(login_data, db)

    