from abc import ABC, abstractmethod
from domain.context import Context

class IAIEngine(ABC):
    @abstractmethod
    def suggest_rules(self, context: Context) -> list[dict]:
        pass

    @abstractmethod
    def feedback(self, results: dict) -> None:
        pass