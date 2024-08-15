from sqlalchemy import update, select
from sqlalchemy.ext.asyncio import AsyncSession

from ..interfaces.user import IUserRepo
from ...schemas.user import User


class UserRepo(IUserRepo):
    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

    async def create(self, user: User) -> None:
        self.session.add(user)
        await self.session.flush()

    async def get(self, user_id: int) -> User | None:
        user = await self.session.get(User, user_id)
        return user

    async def update_locale(self, user_id: int, locale: str) -> None:
        request = update(User).where(User.user_id == user_id).values(locale=locale)
        await self.session.execute(request)
        await self.session.flush()

    async def update_anncmt(self, user_id: int, anncmt: bool) -> None:
        request = update(User).where(User.user_id == user_id).values(anncmt=anncmt)
        await self.session.execute(request)
        await self.session.flush()

    async def update_style(self, user_id: int, style: str) -> None:
        request = update(User).where(User.user_id == user_id).values(style=style)
        await self.session.execute(request)
        await self.session.flush()

    async def get_style(self, user_id: int) -> str | None:
        request = select(User.style).where(User.user_id == user_id)
        return await self.session.scalar(request)
