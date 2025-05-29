import json
from typing import List, Dict, Any

from engine.rule import rule
from domain.context import context
from repositories.rules_file import rules_file

class rule_engine:
    
    def __init__(self, rules: rules_file) -> None:
        self.rules_path = rules
        self.rules: List[rule] = []
        self._json_to_rules()

    def _json_to_rules(self)->None:
        with open(str(self.rules_path),'r') as f:
            rules_json = json.load(f)
        
        self.rules = [rule(r['name'],r['priority'],r['combinable'],r['active'], r['conditions'], r['restrictions'], r['exceptions']) for r in rules_json]
        pass

    def run(self, con: context):
        print("run")
        return List[rule],