from typing import List
from interfaces.i_promo import IPromo
from domain.context import Context
 
class RuleEngine:   
    def __init__(self, rules: List[IPromo]) -> None: # reglas ya instanciadas a evaluar
        self.rules: List[IPromo] = rules

    def evaluate_rules(self, context: Context) -> List[IPromo]:        
        applied_rules: List[IPromo] = []

        for promo in self.rules:
            if promo.evaluate(context):
                print(f"the promo has detonated the actions")
                applied_rules.append(promo)
            
        return applied_rules # Retorna la lista de reglas que resultaron aplicables.