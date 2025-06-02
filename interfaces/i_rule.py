from abc import ABC, abstractmethod
from domain.context import Context

class IRule(ABC): #  Interfaz que define una regla de negocio: debe saber evaluarse (evaluate) y, de ser aplicable, ejecutar efectos (execute).
    @abstractmethod
    def evaluate(self, context: Context) -> bool:
        pass

    def execute(self, context: Context) -> None:
        pass