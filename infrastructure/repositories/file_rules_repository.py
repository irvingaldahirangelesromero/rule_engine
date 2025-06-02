import json
from typing import List
from interfaces.i_rules_file import IRulesFile
from interfaces.i_rule import IRule
from domain.models.rule import Rule #  la clase Rule del dominio

class FileRulesRepository(IRulesFile):
    #     Repositorio que lee un archivo JSON y retorna una lista de instancias de Rule (dominio) usando Rule.from_dict().
    def __init__(self, path_file:str):
        self.path_file = path_file # path_file: ruta al archivo JSON (p. ej. "rules.json")

    
    def upload_rules(self) -> List[IRule]: # Lee el JSON localizado en self.path_file y lo parsea a objetos Rule (instancias del dominio). Retorna lista de IRule.
        try:
            with open(self.path_file, 'r', encoding='utf8') as file:
                data = json.load(file)
        except Exception as e:
            # Aquí podrías lanzar una excepción de negocio personalizada
            raise

        rules: List[IRule] = []
        for r in data:
            rule = Rule.from_dict(r) # # Rule.from_dict construye el objeto de dominio
            rules.append(rule)

        return rules
