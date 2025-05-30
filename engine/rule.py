from typing import List
from interfaces.i_rule import IRule
from interfaces.i_criterion import ICriterion
from interfaces.i_benefit import IBenefit
from interfaces.i_actions import IAction
from domain.context import context

class rule(IRule):
    
    def __init__(self, name: str, conditions: list[ICriterion], exceptions: list[ICriterion], restrictions: list[ICriterion], benefits:list[IBenefit],actions: List[IAction]):
        self.name = name
        self.conditions = conditions
        self.exceptions = exceptions
        self.restrictions = restrictions
        self.benefits = benefits
        self.actions = actions bytes
        
    def run(self, context: context) -> bool:
        for cond in self.conditions:
            if cond.evaluate(context):
                return False 
                    
        for excpt in self.exceptions:
            if excpt.evaluate(context):
                return False
            
        for rest in self.restrictions:
            if rest.evaluate(context):
                return False

        print(f"[Regla: {self.name} Aplicable]")
        self.run_actions(context)  
        return True    
    
    def run_actions(self, context:context)->None:
        for action in self.actions:
            action.run_action(context)