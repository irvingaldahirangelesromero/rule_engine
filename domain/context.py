from typing import Dict, Any

class Context:   
    def __init__(self, code:str, data:Dict[str, Any]): # Solo agrega  datos de la reserva
        self.code = code # promocode
        self.data = data # diccionario de datos necesarios para evaluar criterios

    def get(self, key: str) -> Any: 
        return self.data.get(key) # valor asociado a la clave
    
    def __getitem__(self, key:str) -> Any:
        return self.data[key] # para acceder directamente a self.data