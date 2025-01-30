from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager
from api_v1 import router as router_v1
from core.config import settings
from core.models import db_helper
from actions.create_superuser import create_superuser


@asynccontextmanager
async def lifespan(app:FastAPI): 
    # async with db_helper.engine.begin() as conn:
        # await conn.run_sync(Base.metadata.create_all)
    # await create_superuser()
    yield
    await db_helper.dispose()


app = FastAPI(lifespan=lifespan, debug=True)



app.include_router(router_v1, prefix=settings.api_v1_prefix)




if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
