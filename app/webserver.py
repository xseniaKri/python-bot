from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models import User, Result
from app.db.db import SessionLocal

app = FastAPI()

@app.get("/database")
async def get_users_results():
    async with SessionLocal() as session:
        stmt = select(User, Result).join(Result, Result.user_id == User.user_id)
        result = await session.execute(stmt)
        data = []
        for user, res in result.all():
            data.append({
                "user": {
                    "user_id": user.user_id,
                    "nickname": user.nickname
                },
                "result": {
                    "result_id": res.result_id,
                    "total_score": res.total_score
                }
            })
        return data
