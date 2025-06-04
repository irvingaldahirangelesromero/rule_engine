from abc import ABC, abstractmethod
from domain.context import Context

class ICriterion(ABC):

    @abstractmethod
    def evaluate(self, context: Context) -> bool: 
        pass