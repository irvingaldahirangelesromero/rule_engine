from typing import Dict, Any

class Context:   
    def __init__(self, code:str, data:Dict[str, Any]): 
        self.code = code 
        self.data = data # diccionario de datos necesarios para evaluar criterios

    def getCode(self) -> str:
        return self.code 