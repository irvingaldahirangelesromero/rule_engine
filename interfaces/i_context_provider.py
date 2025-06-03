# Obtiene un Context}desde un servicio externo

from abc import ABC, abstractmethod
from domain.context import Context

class IContextProvider(ABC):
    @abstractmethod
    def get_context(self, code: str) -> Context:
        
        pass
