from typing import List,Dict,Any,Type,Sequence
from interfaces.i_rule import IRule
from interfaces.i_criterion import ICriterion
from interfaces.i_benefit import IBenefit
from interfaces.i_actions import IAction
from domain.context import Context

from domain.genericCriterion import GenericCriterion
from domain.genericBenefit import GenericBenefit
from domain.genericAction import GenericAction

class Rule(IRule):
    
    def __init__(self, name: str, conditions: Sequence[ICriterion], exceptions: Sequence[ICriterion], restrictions: Sequence[ICriterion], benefits:Sequence[IBenefit],actions: Sequence[IAction]):
        self.name = name
        self.conditions = conditions
        self.exceptions = exceptions
        self.restrictions = restrictions
        self.benefits = benefits
        self.actions = actions
    
    def __str__(self) -> str:
        return f"Rule: {self.name}"

 # Evalúa únicamente las condiciones y excepciones/restricciones, y devuelve True si la regla es aplicable.
    def evaluate(self, context: Context) -> bool:
        print(f"[Evaluating rule: {self.name}]")

        for cond in self.conditions: 
            if not cond.evaluate(context):               
                print(f"[rule: {self.name}] condition '{cond}' not is fulfilled : the rule no apply")
                return False 
                    
        for exc in self.exceptions: 
            if exc.evaluate(context):
                print(f"[rule: {self.name}] exception: '{exc}' : the rule no apply")
                return False
            
        for restric in self.restrictions: 
            if not restric.evaluate(context):
                print(f"[rule: {self.name}] restriction '{restric}' not is fulfilled : the rule no apply")
                return False

        print(f"[rule: {self.name} Aplicable], now apply actions and benefits\n")
        return True    
    

    def execute(self, context:Context)->None: # Ejecuta las acciones y aplica beneficios. Esto solo se llama si evaluate(context) devolvió True.
        for action in self.actions:
            action.run_action(context)
            
        for benefits in self.benefits:
            benefits.apply(context)

    @classmethod # permite crear una instancia de la clase
    def from_dict(cls: Type["Rule"], data: Dict[str, Any]) -> "Rule":
        conditions = []
        exceptions = []
        restrictions = []
        benefits = []
        actions = []
   
        #   Instanciación de objetos de dominio a partir del producto json.load
        for c in data.get("conditions", []): # si el json no tiene "conditions" la lista queda vacia
            condition = GenericCriterion.from_dict(c)
            conditions.append(condition)

        for e in data.get("exceptions", []):
            exception = GenericCriterion.from_dict(e)
            exceptions.append(exception)

        for r in data.get("restrictions", []):
            restriction = GenericCriterion.from_dict(r)
            restrictions.append(restriction)

        for b in data.get("benefits", []):
            benefit = GenericCriterion.from_dict(b)
            benefits.append(benefit)

        for a in data.get("actions", []):
            action = GenericCriterion.from_dict(a)
            actions.append(action)
        
        # construya una instancia completamente funcional de la clase Rule
        return cls(data["name"], conditions, exceptions, restrictions, benefits, actions)