from __future__ import annotations

from typing import Sequence

from domain.context import Context

from interfaces.i_rule import IRule
from interfaces.i_criterion import ICriterion
from interfaces.i_benefit import IBenefit
from interfaces.i_actions import IAction

class Rule(IRule):
    
    def __init__(self, name: str, conditions: Sequence[ICriterion], exceptions: Sequence[ICriterion], restrictions: Sequence[ICriterion], benefits:Sequence[IBenefit],actions: Sequence[IAction]):
        self.name = name
        self.conditions = conditions
        self.exceptions = exceptions
        self.restrictions = restrictions
        self.benefits = benefits
        self.actions = actions
    
    def __str__(self) -> str:
        return self.name

 # Evalúa únicamente las condiciones y excepciones/restricciones, y devuelve True si la regla es aplicable.
    def evaluate(self, context: Context) -> bool:
        print(f"[Evaluating rule: {self.name}]")
        for cond in self.conditions: 
            if not cond.evaluate(context):               
                print(f"[rule: {self.name}] condition '{  cond}' not is fulfilled : the rule no apply")
                return False 
                    
        for exc in self.exceptions: 
            if exc.evaluate(context):
                print(f"[rule: {self.name}] exception: '{exc}' : the rule no apply")
                return False
            
        for restric in self.restrictions: 
            if not restric.evaluate(context):
                print(f"[rule: {self.name}] restriction '{restric}' not is fulfilled : the rule no apply")
                return False

        print(f"[the rule: {self.name} is Aplicable], applying actions and benefits\n")
        return True    
    

    def execute(self, context:Context)->None: # Ejecuta las acciones y aplica beneficios. Esto solo se llama si evaluate(context) devolvió True.
        for action in self.actions:
            action.run_action(context)
            
        for benefits in self.benefits:
            benefits.apply(context)

    # @classmethod # permite crear una instancia de la clase
    # def dict_to_rule(cls: Type["Rule"], data: Dict[str, Any]) -> Rule: # Convertir el diccionario en una instancia de Rule.
        # conditions = []
        # exceptions = []
        # restrictions = []
        # benefits = []
        # actions = []
    
        # #   Instanciación de objetos de dominio a partir del producto json.load
        # for c in data.get("conditions", []): # si el json no tiene "conditions" la lista queda vacia
        #     condition = CriterionFactory.dict_to_Criterio(c)
        #     conditions.append(condition)

        # for e in data.get("exceptions", []):
        #     exception = CriterionFactory.dict_to_Criterio(e)
        #     exceptions.append(exception)

        # for r in data.get("restrictions", []):
        #     restriction = CriterionFactory.dict_to_Criterio(r)
        #     restrictions.append(restriction)

        # for b in data.get("benefits", []):
        #     benefit = BenefitFactory.dict_to_benefit(b)
        #     benefits.append(benefit)

        # for a in data.get("actions", []):
        #     action = ActionFactory.dict_to_Action(a)
        #     actions.append(action)
        
        
        # # construya una instancia completamente funcional de la clase Rule
        # return cls(data["name"], conditions, exceptions, restrictions, benefits, actions)