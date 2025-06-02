# Aquí defines la clase Rule, implementando la interfaz IRule.
# Lógica pura de “evaluar criterios” sin dependencias externas.

from typing import List,Dict,Any,Type,Sequence 

from interfaces.i_rule import IRule
from interfaces.i_criterion import ICriterion
from interfaces.i_benefit import IBenefit
from interfaces.i_actions import IAction
from domain.context import Context

class Rule(IRule):
    
    def __init__(self, name: str, conditions: Sequence[ICriterion], exceptions: Sequence[ICriterion], restrictions: Sequence[ICriterion], benefits:Sequence[IBenefit],actions: Sequence[IAction]):
        self.name = name
        self.conditions = conditions
        self.exceptions = exceptions
        self.restrictions = restrictions
        self.benefits = benefits
        self.actions = actions

 # Evalúa únicamente las condiciones y excepciones/restricciones, y devuelve True si la regla es aplicable.
    def evaluate(self, context: Context) -> bool:
        print(f"[Evaluating rule: {self.name}]")

        for cond in self.conditions: # Si algúna condicion NO se cumple, la regla NO aplica
            if not cond.evaluate(context):               
                print(f"[rule: {self.name}] condition '{cond}' not is fulfilled  → the rule no apply")
                return False 
                    
        for exc in self.exceptions: # Verificar excepciones (si se cumple alguna, descartamos la regla)
            if exc.evaluate(context):
                print(f"[rule: {self.name}] exception '{exc}' not is fulfilled  → the rule no apply")
                return False
            
        for restric in self.restrictions: # Verificar restricciones (si alguna NO se cumple, la regla NO aplica)
            if not restric.evaluate(context):
                print(f"[rule: {self.name}] restriction '{restric}' not is fulfilled  → the rule no apply")
                return False

        print(f"[rule: {self.name} Aplicable], now apply actions and benefits")
        return True    
    

    def execute(self, context:Context)->None: # Ejecuta las acciones y aplica beneficios. Esto solo se llama si evaluate(context) devolvió True.
        for action in self.actions:
            action.run_action(context)
            
        for benefits in self.benefits:
            benefits.apply(context)


    @classmethod
    def from_dict(cls: Type["Rule"], data: Dict[str, Any]) -> "Rule":
        from domain.implementations.genericCriterion import GenericCriterion
        from domain.implementations.genericBenefit import GenericBenefit
        from domain.implementations.genericAction import GenericAction
    # Construye una instancia Rule a partir de un dict con la forma:
    # {
    #   "name": "Descuento_nuevo_cliente",
    #   "conditions": [ { ... }, ... ],
    #   "exceptions": [ ... ],
    #   "restrictions": [ ... ],
    #   "benefits": [ { "description": "..." }, ... ],
    #   "actions": [ { "type": "...", ... }, ... ]
    # }

    #   Construir listas de objetos de dominio
        conditions = [GenericCriterion.from_dict(c) for c in data.get("conditions", [])]
        exceptions = [GenericCriterion.from_dict(e) for e in data.get("exceptions", [])]
        restrictions = [GenericCriterion.from_dict(r) for r in data.get("restrictions", [])]
        benefits = [GenericBenefit.from_dict(b) for b in data.get("benefits", [])]
        actions = [GenericAction.from_dict(a) for a in data.get("actions", [])]

        return cls(
            name=data["name"],
            conditions=conditions,
            exceptions=exceptions,
            restrictions=restrictions,
            benefits=benefits,
            actions=actions
        )