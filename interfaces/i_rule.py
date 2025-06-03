from abc import ABC, abstractmethod
from domain.context import Context

class IRule(ABC): #  Interfaz de regla de negocio

    @abstractmethod
    def evaluate(self, context: Context) -> bool:
        pass

    def execute(self, context: Context) -> None:
        pass