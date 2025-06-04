from interfaces.i_criterion import ICriterion
from domain.context import Context
from typing import Any
import operator

class GenericCriterion(ICriterion):    # representa una condición evaluable dinámicamente en un Context
    OPERATORS = {
        "==": operator.eq,
        "!=": operator.ne,
        ">": operator.gt,
        ">=": operator.ge,
        "<": operator.lt,
        "<=": operator.le,
        "in": lambda a, b: a in b,
        "not in": lambda a, b: a not in b
    }

    def __init__(self, field: str, operator_: str, value: Any):
        self.field = field          # p. ej., "cliente.edad"
        self.operator = operator_   
        self.value = value        

    def __str__(self):
        return f"{self.field} {self.operator} {self.value}"
    
    def evaluate(self, context: Context) -> bool: # Evalúa si un campo en el Context cumple una condición
        try:
            parts = self.field.split(".")   # nombre del campo a consultarse en el contexto
            value_context = context.data    
            for part in parts: #  Se recorre cada nivel del campo anidado 
                
                value_context = value_context.get(part) 
                
                if value_context is None: 
                    print(f"[Key '{part}' not found")
                    return False
                
            op_func = self.OPERATORS[self.operator] #  Se obtiene la función correspondiente al operador 
            return op_func(value_context, self.value) # Se aplica la comparación

        except Exception as e:
            print(f"[Error: {e}")
            return False


    @classmethod
    def from_dict(cls, data: dict) -> "GenericCriterion":  
        return cls(data["field"], data["operator"], data["value"])