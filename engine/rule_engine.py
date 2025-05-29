import json
from engine.rule import rule
from typing import List, Dict, Any

class rule_engine:
    
    def __init__(self, rules_path:str) -> None:
        self.rules_path = rules_path
        self.rules: List[rule] = []
        self._json_to_rules()


    def _json_to_rules(self)->None:
        # with open(self.rules_path,'r') as f:
            # rules_json = json.load(f)
        
        # self.rules = [rule(r['name'], r['conditions'],) for r in rules_json]
        pass
    def run(self, context: Dict[str, Any]):
        print("run")