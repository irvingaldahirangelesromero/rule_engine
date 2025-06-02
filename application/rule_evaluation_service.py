# Orquestación para evaluar reglas (sin lógica de negocio)

# Aquí orquestas el flujo total: obtener context, cargar reglas, evaluar, ejecutar acciones/beneficios, combinar con IA si corresponde y devolver resultados. Por ejemplo:

from typing import List
from interfaces.i_rules_file import IRulesFile
from domain.context import Context
from domain.models.rule import Rule
from interfaces.i_rule import IRule
from engine.rule_engine import RuleEngine

class RuleEvaluationService:
    
    # Caso de uso: 'Evaluar reglas para un contexto determinado'.
    # Orquesta:
    #   1) Cargar reglas desde IRulesFile.
    #   2) Para cada regla, invocar Rule.evaluate(context).
    #   3) Si aplica, invocar Rule.execute(context).
    #   4) Devolver un reporte con los resultados de evaluación.
    

    def __init__(self, rules_repository: IRulesFile):
        # Inyectamos el repositorio (FileRulesRepository) que cumplirá IRulesFile
        # Invertimos la dependencia: recibimos la abstracción IRulesFile
        self.rules_repository = rules_repository 

    def evaluate_all(self, context: Context) -> List[IRule]: # Retorna la lista de reglas que se dispararon y ya ejecutaron sus acciones/beneficios.
        reglas: List[IRule] = self.rules_repository.upload_rules() # 1) Obtener reglas del repositorio        
        engine = RuleEngine(reglas) # 2) Inicializar motor
        reglas_aplicadas = engine.evaluate_rules(context) # 3) Evaluar todas las reglas (internamente ejecutará las acciones/beneficios)
        return reglas_aplicadas # 4) Devolver las reglas aplicadas (para logging, reporting, etc.)