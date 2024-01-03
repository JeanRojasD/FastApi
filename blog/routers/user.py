from fastapi import APIRouter, Depends
from .. import database, schemas, models
from sqlalchemy.orm import Session
from ..repository import userRepository

router = APIRouter(
    prefix='/user',
    tags=['Users']
)
get_db = database.get_db


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return userRepository.create(request, db)

@router.get('/{id}',  response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return userRepository.show(id, db)