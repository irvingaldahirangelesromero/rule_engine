# coordinación total de los componentes para evaluar promos para un contexto determinad

from typing import List
from interfaces.i_promo import IPromo 
from interfaces.i_promo_file import IPromosFile
from domain.context import Context
from engine.rule_engine_promo import RuleEngine

class PromoEvaluationService:
    def __init__(self, promos_repository: IPromosFile): # Inyección del repositorio e inversión dea dependencia recibiendo una abstracción
        self.promos_repository = promos_repository 

    def evaluate_all(self, context: Context) -> List[IPromo]: 
        promos: List[IPromo] = self.promos_repository.load_promos() # 1) cargar promos del repositorio        
        engine = RuleEngine(promos) # 2) Inicializar motor

        return engine.evaluate_rules(context)
    
    def evaluate_by_code(self, context: Context)-> List[IPromo]:
        code  = context.getCode()
        promo = self.promos_repository.get_by_code(code)
        if promo and promo.evaluate(context):
            return [promo]      
        return[]
    