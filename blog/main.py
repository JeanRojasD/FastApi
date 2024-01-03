from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blog, user, authentication

# Criar uma instância do FastAPI
app = FastAPI()

# Criar as tabelas no banco de dados, se não existirem
models.Base.metadata.create_all(engine)

# Incluir rotas de outros módulos
app.include_router(blog.router)  # Inclui rotas definidas no módulo blog
app.include_router(user.router)  # Inclui rotas definidas no módulo user
app.include_router(authentication.router)  # Inclui rotas definidas no módulo authentication
