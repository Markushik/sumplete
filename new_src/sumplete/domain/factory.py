from dishka import provide, Provider, Scope

from new_src.sumplete.adapters.database.uow.implement import UnitOfWork
from new_src.sumplete.adapters.redis.adapter.implement import RedisAdapter
from .game.usecase import CreatePuzzle, SaveField
from .user.usecase import UserHandler, UserExist, UserCreate, UpdateLocale


class UsecaseProvider(Provider):
    scope = Scope.REQUEST

    @provide
    async def user_create(self, cache: RedisAdapter, uow: UnitOfWork) -> UserCreate:
        return UserCreate(cache=cache, uow=uow)

    @provide
    async def user_exist(self, cache: RedisAdapter) -> UserExist:
        return UserExist(cache=cache)

    @provide
    async def user_handler(self, exist: UserExist, create: UserCreate) -> UserHandler:
        return UserHandler(exist=exist, create=create)

    @provide
    async def update_locale(self, cache: RedisAdapter, uow: UnitOfWork) -> UpdateLocale:
        return UpdateLocale(cache=cache, uow=uow)

    @provide
    async def field_save(self, uow: UnitOfWork) -> SaveField:
        return SaveField(uow=uow)

    @provide
    async def field_create(self, save: SaveField) -> CreatePuzzle:
        return CreatePuzzle(save=save)
