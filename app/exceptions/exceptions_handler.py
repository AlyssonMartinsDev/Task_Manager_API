from fastapi import FastAPI, Request, status, HTTPException
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletHttpExceptions
from fastapi.responses import JSONResponse


from app.schemas.response_schema import ErrorResponseSchema


class ExceptionHandler:

    @staticmethod
    async def request_validation_error(request: Request, exc: RequestValidationError):

        errors = []

        for error in exc.errors():
            errors.append({
                "field": ".".join(str(loc) for loc in error["loc"][1:]),
                "message": error["msg"]
            })

        error_response = ErrorResponseSchema(
            status=status.HTTP_422_UNPROCESSABLE_ENTITY,
            message="Erro de validação dos dados",
            errors=errors
        )

        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=error_response.model_dump()
        )

    @staticmethod
    async def http_exceptions(request: Request, exc: HTTPException):
        """
            Handler HTTP para lidar com exceções HTTP e retornar respostas apropriadas
            :param request -> Requisição original
            :param exc -> exceção HTTP que ocorreu
        """

        error_response = ErrorResponseSchema(
            status=exc.status_code,
            message=exc.detail,
            errors=[
                {
                "error": str(exc.detail)
                }
            ]
        )

        return JSONResponse(status_code=exc.status_code, content=error_response.model_dump())
    
    










