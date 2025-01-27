from sqlalchemy.ext.asyncio import AsyncSession
from core.models import WhiteList
from sqlalchemy import select, Result, delete
from fastapi import HTTPException, status




async def create_white_list(
                            session: AsyncSession, 
                            white_list: WhiteList
                            )->WhiteList:
    name = select(WhiteList).where(WhiteList.name==white_list.name)
    res = await session.execute(name)
    if res.fetchall():
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f'{white_list.name} already exists'
        )
    w_list = WhiteList(**white_list.model_dump())
    session.add(w_list)
    await session.commit()

    return w_list
    


async def get_white_list(session:AsyncSession)->list[WhiteList]:
    stat = select(WhiteList).order_by(WhiteList.id)
    result:Result = await session.execute(stat)
    white_list = result.scalars().all()
    return list(white_list)


async def delete_white_list(tg_id:str, session:AsyncSession)->None:
    stmt = delete(WhiteList).where(WhiteList.tg_id==tg_id)
    await session.execute(stmt)
    await session.commit()

