from app.db.models import User, Result
from app.db.db import SessionLocal
from sqlalchemy.future import select

async def get_or_create_user(nickname: str):
    async with SessionLocal() as session:
        result = await session.execute(select(User).where(User.nickname == nickname))
        user = result.scalar_one_or_none()
        if user:
            return user
        user = User(nickname=nickname)
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user

async def add_result(user_id: int, total_score: int):
    async with SessionLocal() as session:
        result = Result(user_id=user_id, total_score=total_score)
        session.add(result)
        await session.commit()
