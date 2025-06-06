from abc import ABC, abstractmethod
from domain.context import Context

class IBenefit(ABC):

    @abstractmethod
    def apply(self, context: Context) -> None: 
        pass