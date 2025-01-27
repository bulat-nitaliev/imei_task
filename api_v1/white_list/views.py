from fastapi import APIRouter, status, Depends
from . import crud
from .shemas import WhiteList, CreateWhiteList
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper

router = APIRouter(tags=['WhiteList'])

@router.get('/', response_model=list[WhiteList])
async def get_white_list(session:AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_white_list(session=session)
    


@router.post('/',response_model=WhiteList, status_code=status.HTTP_201_CREATED)
async def create_product(
    white_list: CreateWhiteList,
    session:AsyncSession = Depends(db_helper.session_dependency)
                         ):
    return await crud.create_white_list(
        session=session,
        white_list=white_list
        )
