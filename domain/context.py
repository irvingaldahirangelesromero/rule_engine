# Clase Context (agrega solo datos del pedido)
from typing import Dict, Any

class Context:
    #     Contexto de evaluación que contiene:
    
    def __init__(self, code:str, data:Dict[str, Any]):
        self.code = code # code: identificador (por ejemplo, código de descuento)
        self.data = data # data: diccionario con todos los datos necesarios para evaluar criterios

    def get(self, key: str) -> Any: # Devuelve el valor asociado a la clave en el diccionario interno
        return self.data.get(key)
    
    def __getitem__(self, key:str) -> Any:
        # Permite usar context["usuario"] para accceder directamente a self.data
        return self.data[key]