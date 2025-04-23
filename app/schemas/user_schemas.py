from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    username: str = Field(..., title="Nome de usuário", description="Nome único para login do usuário", min_length=3, max_length=50, example="Joe doh")
    email: EmailStr = Field(..., title="Email", description="Endereço de email válido", example="Jow@email.com")

    
class UserCreate(UserBase):
    password: str = Field(..., title="Senha", description="Senha do usuário ( minímo de 8 caracteres)", min_length=8, example="SenhaForte123")
    confirm_password: str = Field(..., title="Confirmação da senha", description="Confirmação da senha.", min_length=8, example="SenhaForte123")


class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True