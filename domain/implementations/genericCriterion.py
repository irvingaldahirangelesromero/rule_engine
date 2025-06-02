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
        self.field = field # field: ruta en el diccionario de context, p. ej., "pedido.total"
        self.operator = operator_         # operator_: cadena que coincide con una key en OPERATORS
        self.value = value         # value: valor de comparación


    def evaluate(self, context: Context) -> bool:
        # Intenta extraer del Context el valor según self.field y compararlo
        # con self.value usando el operador correspondiente.
        try:
            parts = self.field.split(".")
            value_context = context.data  # context.data es un dict
            for part in parts:
                if not isinstance(value_context, dict):
                    print(f"[GenericCriterion] Esperado dict para '{part}', se recibió {type(value_context).__name__}")
                    return False
                value_context = value_context.get(part)
                if value_context is None:
                    print(f"[GenericCriterion] Clave '{part}' no encontrada")
                    return False
            op_func = self.OPERATORS[self.operator]
            return op_func(value_context, self.value)

        except Exception as e:
            # Aquí podrías usar logger en vez de print
            print(f"[GenericCriterion] Error al evaluar criterio: {e}")
            return False


    @classmethod
    # Crea un GenericCriterion a partir de un dict con la forma:
    #     {
    #       "field": "pedido.total",
    #       "operator": ">=",
    #       "value": 100.0
    #     }

    def from_dict(cls, data: dict) -> "GenericCriterion":  
        return cls(
            field=data["field"],
            operator_=data["operator"],
            value=data["value"]
        )
