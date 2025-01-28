from fastapi import APIRouter, Depends
from .white_list.views import router as white_list_router
from .imei.views import router as imei_router
from .auth import router as auth_router
from .users import router as users_router
from fastapi.security import HTTPBearer

http_bearer = HTTPBearer(auto_error=False)

router = APIRouter(
    dependencies=[Depends(http_bearer),]
)
router.include_router(router=white_list_router, prefix='/white_list')
router.include_router(router=imei_router, prefix='/check-imei')
router.include_router(router=auth_router)
router.include_router(router=users_router)
