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

        print(f"[the rule: ''{self.name}'' is Aplicable]\nApplying actions and benefits: []\n")
        return True    
    

    def execute(self, context:Context)->None: # Ejecuta las acciones y aplica beneficios. Esto solo se llama si evaluate(context) devolvió True.
        for action in self.actions:
            action.run_action(context)
            
        for benefits in self.benefits:
            benefits.apply(context)