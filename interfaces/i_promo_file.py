from abc import ABC, abstractmethod
from typing import List
from interfaces.i_promo import IPromo

class IPromosFile(ABC): # para cargar reglas y devuelven list[IRule].
    @abstractmethod
    def load_promos(self)->List[IPromo]:
        pass 