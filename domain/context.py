from typing import Dict, Any

class context:
    def __init__(self, code:str, data:Dict[str, Any]):
        self.code = code
        self.data = data

    def get(self, key: str) -> Any:
        return self.data.get(key)
    
    def __getitem__(self, key:str) -> str:
        return self.data[key]
    