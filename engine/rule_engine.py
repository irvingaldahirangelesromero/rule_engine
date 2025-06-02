from typing import List
from interfaces.i_rule import IRule
from domain.context import Context

class RuleEngine:   
    def __init__(self, rules: List[IRule]) -> None: # reglas ya instanciadas a evaluar
        self.rules: List[IRule] = rules

    def evaluate_rules(self, context: Context) -> List[IRule]:        
        applied_rules: List[IRule] = []

        for rule in self.rules:
            if rule.evaluate(context):
                print(f"the rule has detonated the actions")
                rule.execute(context) # Si la regla es aplicable, ejecutamos acciones y beneficios
                applied_rules.append(rule)
            else:
                print(f"invalid rule")
                pass
            
        return applied_rules # Retorna la lista de reglas que resultaron aplicables.