from typing import List
from domain.rule import Rule
from domain.promo import Promo
from interfaces.i_rule import IRule
from interfaces.i_promo import IPromo
from factories.rule_factory import RuleFactory

class PromoFactory:
    @staticmethod
    def dict_to_promo(data: dict)-> IPromo:    
        code = data["code"] 
        name = data.get("name", "")
        rules_data = data.get("rules",[]) # Obtenemos la lista de reglas desde el diccionario de entrada 'data';
        
        rules: List[IRule]= [] # Lista para ir almacenando las instancias de Rule.

        for rule_dict in rules_data:            # Iteramos cada diccionario de regla presente en 'rules_data'.
            rule = RuleFactory.dict_to_rule(rule_dict)    
            rules.append(rule)                  
   
        return Promo(code,name,rules)