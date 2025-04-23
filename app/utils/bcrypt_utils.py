from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class BcryptUtils:


    @staticmethod
    def create_hash(string: str) -> str:
        """
            Gera uma hash usando o algoritmo Bcrypt
            :param string: string para ser convertida em hash
            :return hash da string fornecida
        """

        return pwd_context.hash(string)
    
    @staticmethod
    def verify_hash(plain_password: str, hased_password: str) -> bool:
        """
            Verifica se a senha em texto simples corresponde à hash fornecida
            :param plain_password: senha em texto simples a ser verificada
            :param hased_password: hash da senha a ser comparada
            :return True se as senhas correspondem, False caso contrário
        """

        return pwd_context.verify(plain_password, hased_password)
    

    