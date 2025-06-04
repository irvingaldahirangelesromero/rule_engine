from typing import Dict, Any
from domain.rule import Rule
from typing import List
from ..factories.criterion_factory import CriterionFactory
from ..factories.benefit_factory import BenefitFactory
from ..factories.action_factory import ActionFactory
from interfaces.i_criterion import ICriterion
from interfaces.i_benefit import IBenefit
from interfaces.i_actions import IAction

class RuleFactory:
    @staticmethod
    def dict_to_rule(data: Dict[str, Any]) -> Rule: # Convertir el diccionario en una instancia de Rule.
        conditions: List[ICriterion] = []
        exceptions: List[ICriterion] = []
        restrictions:List[ICriterion] = []
        benefits:List[IBenefit] = []  
        actions:List[IAction] = []   
    
        #   Instanciación de objetos a partir del producto json.load
        for c in data.get("conditions", []): # si el json no tiene "conditions" la lista queda vacia
            condition = CriterionFactory.dict_to_criterion(c)
            conditions.append(condition)

        for e in data.get("exceptions", []):
            exception = CriterionFactory.dict_to_criterion(e)
            exceptions.append(exception)

        for r in data.get("restrictions", []):
            restriction = CriterionFactory.dict_to_criterion(r)
            restrictions.append(restriction)

        for b in data.get("benefits", []):
            benefit = BenefitFactory.dict_to_benefit(b)
            benefits.append(benefit)

        for a in data.get("actions", []):
            action = ActionFactory.dict_to_action(a)
            actions.append(action)
        
        # construya una instancia completamente funcional de la clase Rule
        return Rule(data["name"], conditions, exceptions, restrictions, benefits, actions)