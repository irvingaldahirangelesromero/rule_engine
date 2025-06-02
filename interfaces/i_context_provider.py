from abc import ABC, abstractmethod
from domain.context import Context

class IContextProvider(ABC):
    @abstractmethod
    def get_context(self, code: str) -> Context:
        # Obtiene un Context (del pedido, usuario, etc.) desde un servicio externo
        # dado el código de descuento u otro identificador.
        pass
