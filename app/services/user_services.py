from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

# Schemas
from app.schemas.response_schema import SuccessResponseSchema
from app.schemas.user_schemas import UserCreate, UserResponse

# Model
from app.models.user_models import User

# Utils
from app.utils.bcrypt_utils import BcryptUtils




class UserService:

    @staticmethod
    def create_new_user(user_data: UserCreate, db: Session):
        """
            Função responsavél por validar e criar um novo usuario no banco de dados
            :param user_data -> Dados filtrados e validados pelo schema para criação do usuário
            :param db -> Sessão do banco de dados utilizada para persistir o novo usuário


        """

        # I- Verifica se ja existe um usuario tanto pelo email quanto pelo nome de usuário.
        existing_user = db.query(User).filter((User.email == user_data.email) | (User.username == user_data.username)).first()

        if existing_user: raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email ou nome de usuario já cadastrado no banco de dados."
        )

        # II- Verifica se a senha e a confirmação da senha são iguais.

        if user_data.password != user_data.confirm_password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="As senhas não coincidem."
            )
    
        # III- Criando a Hash da senha para salvar no banco de dados com segurança.

        hashed_password = BcryptUtils.create_hash(user_data.password)

        # IV- Criando o objeto para criar um novo usuario

        new_user = User(
            email=user_data.email, 
            username=user_data.username, 
            password=hashed_password
        )

        # V- Adiciona, e salva o usuario no banco de dados
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        # VI- Retorna a resposta com os dados do novo usuario

        return new_user
    
    def get_all_users(db: Session):
        """
            Service responsavel por obter todos os usuarios no banco de dados

        """


        