from typing import Dict, Any

class rule:
    
    def __init__(self, name:str, priority: int, combinable: bool, active: bool,  conditions: Dict[str, Any], restrictions: Dict[str, Any], exceptions: Dict[str, Any], action:str) -> None:
        self.name = name
        self.priority = priority
        self.combinable = combinable
        self.active = active
        self.conditions = conditions
        self.restrictions = restrictions
        self.exceptions = exceptions
        self.action = action

    def _str_ (self) -> str: 
        return f"Rule(name: ´{self.name}´\n,Rule(active: ´{self.active}´\n,Rule(conditions: ´{self.conditions}´\n,Rule(restrictions: ´{self.restrictions}´\n, Rule(exceptions: ´{self.exceptions}´\n)"