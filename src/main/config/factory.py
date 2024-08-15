from dishka import provide, Provider, Scope

from src.main.config.models import (
    CommonConfig,
    BotConfig,
    Config,
    DatabaseConfig,
    RedisConfig,
    NatsConfig,
)


class ConfigProvider(Provider):
    scope = Scope.APP

    def __init__(self, config: Config):
        super().__init__()
        self.config = config

    @provide
    def get_config(self) -> Config:
        return self.config

    @provide
    def get_bot_config(self) -> BotConfig:
        return self.config.bot

    @provide
    def get_common_config(self) -> CommonConfig:
        return self.config.common

    @provide
    def get_database_config(self) -> DatabaseConfig:
        return self.config.database

    @provide
    def get_redis_config(self) -> RedisConfig:
        return self.config.redis

    @provide
    def get_nats_config(self) -> NatsConfig:
        return self.config.nats
