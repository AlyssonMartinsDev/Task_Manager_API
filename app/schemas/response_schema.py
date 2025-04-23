from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List, Union


class ResponseSchema(BaseModel):
    status: int = Field(..., title="Status da requisição", description="Status HTTP que a requisição obteve.")
    message: str = Field(..., title="Mensagem da resposta", description="Mensagem detalhando o resultado da requisição.")

class ValidationErrorDetail(BaseModel):
    field: str
    message: str

class HttpExceptionsDetail(BaseModel):
    error: str

class ErrorResponseSchema(ResponseSchema):
    errors: Optional[
        List[Union[ValidationErrorDetail, HttpExceptionsDetail]] ] = Field(None, title="Erros da requisição", description="Lista contendo detalhes sobre os erros que ocorreram.")

class SuccessResponseSchema(ResponseSchema):
    data: Any = Field(..., title="Dados da resposta", description="Dicionário contendo os dados retornados pela requisição.")