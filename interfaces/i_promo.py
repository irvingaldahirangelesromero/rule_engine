from abc import ABC, abstractmethod

from domain.context import Context
# from typing import List
# from interfaces.i_rule import IRule 

class IPromo(ABC):  

    @abstractmethod
    def evaluate(self, context: Context) -> bool:
        pass
    
    @abstractmethod
    def get_codigo(self) -> str:
        pass

    @abstractmethod
    def get_nombre(self) -> str:
        pass