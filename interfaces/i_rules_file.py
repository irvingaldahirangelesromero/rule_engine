from abc import ABC, abstractmethod
from typing import List
from interfaces.i_rule import IRule

class IRulesFile(ABC): # Interfaz para cargar reglas y devuelven list[IRule].
    @abstractmethod
    def load_rules(self)->List[IRule]:
        pass