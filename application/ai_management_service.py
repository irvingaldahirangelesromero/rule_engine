from domain.context import Context
from interfaces.i_ai_engine import IAIEngine
from engine.rule_engine import RuleEngine
from application.rule_evaluation_service import RuleEvaluationService

class AIWithRuleService:
    
    # Caso de uso que combina IA para sugerir reglas dinámicas
    # y luego las evalúa como las reglas estáticas.
    
    def __init__(self, ai_engine: IAIEngine, rules_repository, rule_eval_service: RuleEvaluationService):
        self.ai_engine = ai_engine
        self.rules_repository = rules_repository
        self.rule_eval_service = rule_eval_service

    def evaluate_with_ai(self, context: Context):
        # 1) Obtener reglas estáticas
        reglas_estaticas = self.rules_repository.upload_rules()

        # 2) Obtener reglas dinámicas de IA
        from ai.ai_rules_evaluation import AIRuleEvaluator
        ai_evaluator = AIRuleEvaluator(self.ai_engine)
        reglas_dinamicas = ai_evaluator.get_dynamic_rules(context)

        # 3) Unir ambas listas
        todas_las_reglas = reglas_estaticas + reglas_dinamicas

        # 4) Evaluar todo con RuleEngine
        motor = RuleEngine(todas_las_reglas)
        reglas_aplicadas = motor.evaluate_rules(context)

        # 5) Retornar resultados
        return reglas_aplicadas