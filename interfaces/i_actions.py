from abc import ABC, abstractmethod
from domain.context import context

class IAction(ABC): 
    @abstractmethod
    def run_action(self, context:context)->None:
        pass