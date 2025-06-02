# clase RuleEngine que recibe List[Rule]

import json

from typing import List
from interfaces.i_rule import IRule
from domain.context import Context


class RuleEngine:
    # Motor de reglas que recibe una lista de objetos Rule (dominio) y un Context,
    # evalúa cada regla, ejecuta sus acciones/beneficios y retorna
    # la lista de reglas que se dispararon.
    
    def __init__(self, rules: List[IRule]) -> None:
        self.rules: List[IRule] = []  # Recibimos la lista de reglas ya instanciadas que deberá evaluar

    def evaluate_rules(self, context: Context) -> List[IRule]:
        # Itera sobre todas las reglas, llama a evaluate() y, si es True,
        # invoca execute().
        # Retorna la lista de reglas que resultaron aplicables.
        
        applied_rules: List[IRule] = []

        for rule in self.rules:
            if rule.evaluate(context): # 1) Evaluar la regla
                # Si la regla es aplicable, ejecutamos acciones y beneficios
                print(f"the rule has detonated the actions")
                rule.execute(context)
                applied_rules.append(rule)
            else:
                print(f"invalid rule")
                pass
            
        return applied_rules


                  

