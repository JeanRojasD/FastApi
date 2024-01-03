from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database, models
from ..repository import blogRepository

# Cria uma instância de APIRouter para organizar as rotas relacionadas a blogs
router = APIRouter(
    prefix="/blog",
    tags=['Blogs']  # Categoriza as rotas como pertencentes à tag 'Blogs' para documentação
)

# Obtém a função get_db do módulo database para obter uma instância do banco de dados
get_db = database.get_db

# Rota para obter todos os blogs
@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db)):
    return blogRepository.get_all(db)

# Rota para criar um novo blog
@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    return blogRepository.create(request, db)

# Rota para excluir um blog com um ID específico
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return blogRepository.destroy(id, db)

# Rota para atualizar um blog com um ID específico
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    # Para fins de facilitar o entendimento, usaremos o metodo Put, pois engloba todas as caracteristicas utilizadas nos outros
    """
    Parâmetros:
    - `id`: ID do blog a ser atualizado, fornecido como parte da URL.
    - `request`: Dados do blog a serem atualizados, fornecidos no corpo da requisição.
    - `db`: Uma instância da sessão do banco de dados. O FastAPI fornece automaticamente utilizando Depends(get_db).
    """
    return blogRepository.update(id, request, db)

# Rota para obter um blog específico com um ID específico
@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(get_db)):
    return blogRepository.show(id, db)
