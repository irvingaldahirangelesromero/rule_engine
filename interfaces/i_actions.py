from abc import ABC, abstractmethod
from domain.context import Context

class IAction(ABC): 
    @abstractmethod
    def run_action(self, context:Context)->None: # Ejecuta la acción asociada a este objeto usando los datos que hay en Context.
        pass