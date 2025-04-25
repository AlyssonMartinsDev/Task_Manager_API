from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.auth_schemas import AuthSchemas

from app.utils.bcrypt_utils import BcryptUtils

from app.models.user_models import User

class AuthService:
    @staticmethod
    def login(data: AuthSchemas, db: Session):
        """
            Service resposavel pelo login, e retornar os dados do usuario junto com um token
            :param data = dados de entrada oara login
            :param db = Sessao do banco de dados
            :retur dados resultante do login bem sucedido ou nao 
        """

        # I -Verifica se o usuario existe no banco de dados, se nao existir retorna usuario nao encontrado 
        print(data)
        
        existing_user = db.query(User).filter((User.email == data.credential) | (User.username == data.credential)).first()
        print(existing_user)
        
        if not existing_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuário não encontrado"
            )