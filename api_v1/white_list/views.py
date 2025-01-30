from fastapi import APIRouter, status, Depends
from . import crud
from .shemas import WhiteList, CreateWhiteList
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from api_v1.fastapi_users import current_user, current_super_user
from typing import Annotated
from core.models.user import User
from core.schemas.user import UserShema

router = APIRouter(tags=['WhiteList'])

@router.get('/', response_model=list[WhiteList])
async def get_white_list(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_dependency)
        ] ,
    user: Annotated[
        User,
        Depends(current_user)
    ] ):
    return await crud.get_white_list(session=session)
    


@router.post('/',response_model=WhiteList, status_code=status.HTTP_201_CREATED)
async def create_product(
    white_list: CreateWhiteList,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_dependency)
        ] ,
    user: Annotated[
        User,
        Depends(current_super_user)
          ]               ):
    return await crud.create_white_list(
        session=session,
        white_list=white_list
        )


@router.delete('/{tg_id}')
async def delete_by_tg_id(
    tg_id:str, 
    session:AsyncSession = Depends(db_helper.session_dependency)
    ):
    await crud.delete_white_list(
        tg_id=tg_id, 
        session=session
        )


@router.get('/list_users', response_model=list[UserShema])
async def get_users(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_dependency)
        ] ,
    user: Annotated[
        User,
        Depends(current_super_user)
          ]
):
    return await crud.get_list_users(session=session)