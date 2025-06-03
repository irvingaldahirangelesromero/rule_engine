from interfaces.i_actions import IAction
from domain.context import Context

class GenericAction(IAction):

    def __init__(self, type_: str, params: dict):
        self.type = type_ # tipo o nombre de la acción 
        self.params = params # diccionario de parámetros para esa acción (por ejemplo, porcentaje de descuento, email, etc.)

    def run_action(self, context: Context) -> None:
        print(f"[ACTION] Executing action of kind: {self.type} with the params: {self.params}")

    @classmethod
   
    def from_dict(cls, data: dict) -> "GenericAction":
        type_value = data["type"]
        params = {}

        for key, value in data.items():
            if key != type:
                params[key] = value  # construye un nuevo diccionario con todos los pares excepto aquel cuya clave sea "type
        
        return cls(type_value,params)