from __future__ import annotations
from typing import List, Dict, Any
from domain.rule import Rule
from domain.context import Context
from interfaces.i_rule import IRule
from interfaces.i_promo import IPromo
from .factories.rule_factory import RuleFactory

class Promo(IPromo):
    def __init__(self, code: str, name: str, rules: List[IRule]):
        self.code = code
        self.name = name 
        self.rules = rules

    def get_codigo(self) -> str:
        return self.code

    def get_nombre(self) -> str:
        return self.name

    def evaluate(self, context: Context) -> bool:
        print(f"\n[evaluating promo: '{self.code}' : ''{self.name}'']")
        all_apply = True

        for rule in self.rules:
            result = rule.evaluate(context)
            if result:
                print(f"The rule '{rule}' apply correctly")
            else:
                print(f"The rule '{rule}' no apply.")
                all_apply = False

        if all_apply:
            print(f"[Promotion '{self.code}' is aplicable]\n")
        else:
            print(f"[Promotion '{self.code}' is not aplicable]\n")
        return all_apply