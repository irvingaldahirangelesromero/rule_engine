from abc import ABC, abstractmethod
from domain.context import context

class IRule(ABC):

    @abstractmethod
    def run(self, context: context) -> bool:
        pass