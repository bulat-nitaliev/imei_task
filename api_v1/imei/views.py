from fastapi import APIRouter
from .schemas import Imei
from core.config import settings
from .crud import create_check


router = APIRouter(tags=['Imei'])

@router.post('/')
async def data_imei(imei:Imei):
    return await create_check(
        url=settings.url_api, 
        api_key=settings.api_key,
        imei=imei.imei_or_sn)

