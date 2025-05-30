from abc import ABC, abstractmethod
from domain.context import context

class IBenefit(ABC):

    @abstractmethod
    def apply(self, context: context) -> None:
        pass
