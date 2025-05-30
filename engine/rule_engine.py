import json
from typing import List

from engine.rule import rule
from services.actions import run_action

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
        self.rules = [rule(r['name'],r['priority'],r['combinable'],r['active'], r['conditions'], r['restrictions'], r['exceptions'], r['action']) for r in rules_json]

    def evaluate_rules(self, context:context)->None:   
        for rule in self.rules:
            if self.rule_is_valid(rule, context):
                print(f"the rule: '{rule.name}' has detonated the action: '{rule.action}'")
                run_action(rule.action, context)
            else:
                print(f"invalid rule")
                  
    def rule_is_valid(self, rule:rule, context:context) -> bool:
        for field, condition in rule.conditions.items():
            if field not in context.data:
                return False
            
            value_context = context[field]
        return True

            
