from fastapi import APIRouter
from .white_list.views import router as white_list_router
from .imei.views import router as imei_router

router = APIRouter()
router.include_router(router=white_list_router, prefix='/white_list')
router.include_router(router=imei_router, prefix='/check-imei')
