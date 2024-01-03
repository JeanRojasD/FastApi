from passlib.context import CryptContext

# Criar uma instância do CryptContext para lidar com hashing de senha
pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Classe para lidar com operações de hash
class Hash():
    
    # Método para gerar um hash usando o algoritmo bcrypt
    @staticmethod
    def bcrypt(password: str):
        # Retorna o hash da senha usando a instância do CryptContext
        return pwd_cxt.hash(password)
    
    def verify(hashed_password, plain_password):
        return pwd_cxt.verify(plain_password, hashed_password)
