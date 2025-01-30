from fastapi import APIRouter, Depends
from .schemas import Imei
from core.config import settings
from .crud import create_check
from typing import Annotated
from core.models.user import User
from api_v1.fastapi_users import current_user


router = APIRouter(tags=['Imei'])

@router.post('/')
async def data_imei(
    imei:Imei,
    user: Annotated[
        User,
        Depends(current_user)
    ]
    ):
    return await create_check(
        url=settings.url_api, 
        api_key=settings.api_key,
        imei=imei.imei_or_sn)

