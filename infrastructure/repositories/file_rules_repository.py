import json
from typing import List
from interfaces.i_rules_file import IRulesFile
from interfaces.i_rule import IRule
from domain.rule import Rule 

class FileRulesRepository(IRulesFile):
    def __init__(self, path_file:str):
        self.path_file = path_file # Ruta de reglas

    def load_rules(self) -> List[IRule]:
        try:
            with open(self.path_file, 'r', encoding='utf8') as file: # 'r': modo de apertura del archivo 
                data = json.load(file)
        except Exception as e:
            raise

        rules: List[IRule] = []
        for r in data: 
            rule = Rule.from_dict(r) # Parseo a objetos Rule
            rules.append(rule)

        return rules