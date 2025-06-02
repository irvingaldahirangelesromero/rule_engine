# Implementa IRulesFile (lee rules.json)

from abc import ABC, abstractmethod
from typing import List
from interfaces.i_rule import IRule

class IRulesFile(ABC): # Interfaz para repositorios que cargan reglas desde alguna fuente (archivo, BD, etc.) y devuelven list[IRule].
    @abstractmethod
    def upload_rules(self)->List[IRule]:
        pass