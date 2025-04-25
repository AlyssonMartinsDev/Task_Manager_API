from pydantic import BaseModel, EmailStr, Field
from typing import Union

class AuthSchemas(BaseModel):
    credential: Union[str, EmailStr] = Field(..., title="Credencial de entrada", description="Credencial para realizar o login (email ou username)" )
    password: str = Field(..., title="Senha", description="Senha do usuário ( minímo de 8 caracteres)", min_length=8, example="SenhaForte123")
