# representa una condición evaluable dinámicamente en un Context

from interfaces.i_criterion import ICriterion
from domain.context import Context
from typing import Any
import operator

class GenericCriterion(ICriterion):
     #  Criterio genérico que evalúa un campo del contexto usando un operador y un valor de comparación.
    
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
        self.field = field          # ruta en el diccionario de context, p. ej., "pedido.total"
        self.operator = operator_   
        self.value = value        


    def evaluate(self, context: Context) -> bool:
        try:
            parts = self.field.split(".")   # nombre del campo a consultarse en el contexto
            value_context = context.data    #l lugar donde están todas las variables dinámicas.
            for part in parts: #  Se recorre cada nivel del campo anidado 

                if not isinstance(value_context, dict): # Si en algún moomento se espera un diccionario pero no lo es se devuelve false
                    print(f"[GenericCriterion] Esperado dict para '{part}', se recibió {type(value_context).__name__}")
                    return False
                
                value_context = value_context.get(part) # se extrae el valor del siguiente nivel del contexto.
                
                if value_context is None:
                    print(f"[GenericCriterion] Clave '{part}' no encontrada")
                    return False
                
            op_func = self.OPERATORS[self.operator] #  Se obtiene la función correspondiente al operador 
            return op_func(value_context, self.value) # Se aplica la comparación

        except Exception as e:
            print(f"[GenericCriterion] Error al evaluar criterio: {e}")
            return False


    @classmethod
    def from_dict(cls, data: dict) -> "GenericCriterion":  
        return cls(data["field"], data["operator"], data["value"])