from interfaces.i_ai_engine import IAIEngine
from domain.context import Context
from domain.models.rule import Rule

class AIRuleEvaluator:
    
    # Lógica de dominio puro que, dada una implementación de IAIEngine, solicita a la IA que sugiera reglas y las convierte en instancias Rule.
    
    def __init__(self, ai_engine: IAIEngine):
        self.ai_engine = ai_engine

    def get_dynamic_rules(self, context: Context) -> list[Rule]:       
        reglas_dicts = self.ai_engine.suggest_rules(context) # 1) Solicita a la IA definiciones de reglas
        reglas: list[Rule] = []

        for rd in reglas_dicts: # 2) Convierte cada dict en instancia Rule usando Rule.from_dict()
            regla = Rule.from_dict(rd)
            reglas.append(regla)

        return reglas
