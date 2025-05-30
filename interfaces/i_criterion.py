from abc import ABC, abstractmethod
from domain.context import context

class ICriterion(ABC):

    @abstractmethod
    def evaluate(self, context: context) -> bool:
        pass
