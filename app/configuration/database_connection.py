import logging
from typing import Union

from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from sqlalchemy.util import classproperty

from app.configuration.configuration import Configuration
from app.utils.exceptions import DatabaseConnectionFailureException
from sqlalchemy import text


class DatabaseConnection():
    _connection: AsyncEngine | None = None
    logger = logging.getLogger()


    @classproperty
    def connection(cls) -> AsyncEngine | None:
        if not cls._connection:
            cls.init_connection()
        return cls._connection

    @classmethod
    def init_connection(cls) -> None:
        db_name, host, user, password = Configuration.get_db_connection_info()
        try:
            cls._connection = create_async_engine(f'postgresql+asyncpg://{user}:{password}@{host}/{db_name}')
        except:
            cls.logger.exception(f"Failed connection to database {db_name}")
            raise DatabaseConnectionFailureException
        cls.logger.debug(f"{user} connection to database {db_name} established")

    @classmethod
    async def execute_query(cls, query: str) -> list[Union[dict | None]]:
        async with cls._connection.connect() as conn:
            cls.logger.debug(f"Executing query: {query}")
            data = await conn.execute(text(query))
            return [row._asdict() for row in data] if data else []