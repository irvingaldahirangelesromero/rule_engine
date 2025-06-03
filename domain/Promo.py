from typing import List, Dict, Any
from domain.rule import Rule
from domain.context import Context
from interfaces.i_rule import IRule
from interfaces.i_promo import IPromo

class Promo(IPromo):
    def __init__(self, code: str, name: str, rules: List[IRule]):
        self.code = code
        self.name = name 
        self.rules = rules

    def get_codigo(self) -> str:
        return self.code

    def get_nombre(self) -> str:
        return self.name

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Promo":
        code = data["code"] 
        name = data.get("name", "")
        rules_data = data.get("rules",[]) # Obtenemos la lista de reglas desde el diccionario de entrada 'data';
        
        rules: List[IRule]= [] # Lista para ir almacenando las instancias de Rule.

        for rule_dict in rules_data:            # Iteramos cada diccionario de regla presente en 'rules_data'.
            rule = Rule.from_dict(rule_dict)    
            rules.append(rule)                  

        return cls(code,name,rules)


    def evaluate(self, context: Context) -> bool:
        print(f"\n[evaluating promo: {self.code} : {self.name}]")
        all_apply = True

        for rule in self.rules:
            result = rule.evaluate(context)
            if result:
                print(f" The rule '{rule}' apply correctly")
            else:
                print(f" The rule '{rule}' no apply.")
                all_apply = False

        if all_apply:
            print(f"[Promoción '{self.code}' aplicable]\n")
        else:
            print(f"[Promoción '{self.code}' not aplicable]\n")
        return all_apply