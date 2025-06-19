from app.db.models import Users
from app.db.db import SessionLocal
from sqlalchemy.future import select
from typing import Dict


async def add_result(user_id: int, nickname: str, result: int, hard: str) -> None:
    async with SessionLocal() as session:
        stmt = select(Users).filter_by(user_id=user_id)
        result_obj = await session.execute(stmt)
        existing = result_obj.scalar_one_or_none()
        if existing:
            existing.nickname = nickname
            existing.result = result
            existing.hard = hard
        else:
            new_user = Users(user_id=user_id, nickname=nickname, result=result, hard=hard)
            session.add(new_user)

        await session.commit()

async def get_result(user_id: int) -> Dict[str, any] | None:
    async with SessionLocal() as session:
        stmt = select(Users).filter_by(user_id=user_id)
        result_obj = await session.execute(stmt)
        existing = result_obj.scalar_one_or_none()

        nickname = existing.nickname
        result = existing.result
        hard = existing.hard

        return {"nickname": nickname,
                "result": result,
                "hard": hard}

