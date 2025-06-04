# coordinación total de los componentes para evaluar reglas para un contexto determinad

from typing import List
from interfaces.i_rule import IRule
from interfaces.i_rules_file import IRulesFile
from domain.context import Context
from engine.rule_engine import RuleEngine

class RuleEvaluationService:
    def __init__(self, rules_repository: IRulesFile): # Inyección del repositorio e inversión dea dependencia recibiendo una abstracción
        self.rules_repository = rules_repository 

    def evaluate_all(self, context: Context) -> List[IRule]: 
        reglas: List[IRule] = self.rules_repository.load_rules() # 1) cargar reglas del repositorio        
        
        engine = RuleEngine(reglas) # 2) Inicializar motor
        
        reglas_aplicadas = engine.evaluate_rules(context) # 3) Evaluar todas las reglas
        return reglas_aplicadas # Reglas aplicadas y disparadasñÑ