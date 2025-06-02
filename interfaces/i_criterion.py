from abc import ABC, abstractmethod
from domain.context import Context

class ICriterion(ABC):

    @abstractmethod
    def evaluate(self, context: Context) -> bool: # Devuelve True si el criterio se cumple bajo el Context dado, False en caso contrario.
        pass

    