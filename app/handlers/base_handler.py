from abc import ABC, abstractmethod

class BaseHandler(ABC):

    @property
    @abstractmethod
    def path(self) -> str:
        ...

    @property
    @abstractmethod
    def method(self) -> [str]:
        ...

    @abstractmethod
    async def callback_handler(self, *args, **kwargs) -> dict:
        ...