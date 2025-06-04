from abc import ABC, abstractmethod
from typing import List
from interfaces.i_promo import IPromo

class IPromosFile(ABC):
    @abstractmethod
    def load_promos(self)->List[IPromo]:
        pass 

    @abstractmethod
    def get_by_code(self, code:str)-> IPromo | None:
        pass