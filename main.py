from infrastructure.repositories.file_rules_repository import FileRulesRepository
from application.rule_evaluation_service import RuleEvaluationService
from domain.context import Context

def main():
    # 1. Preparar repositorio de reglas (archivo JSON)
    rules_repo = FileRulesRepository("rules.json")  
    rule_service = RuleEvaluationService(rules_repository=rules_repo)

    # 2. Simular datos de contexto (por ejemplo, datos de un pedido)
    datos_contexto = {
        "usuario": {"es_cliente_nuevo": True, "email": "juan@example.com"},
        "pedido": {"total": 150.0}
        # ... cualquier otra clave que tus criterios necesiten
    }
    con = Context(code="DESC-NUEVO-CLI", data=datos_contexto)

    # 3. Evaluar reglas (sin IA, solo estáticas)
    reglas_aplicadas = rule_service.evaluate_all(con)

    # 4. Mostrar resultados por pantalla
    if reglas_aplicadas:
        print("Se aplicaron las siguientes reglas:")
        for regla in reglas_aplicadas:
            print(f"  • {regla}")
    else:
        print("No se aplicó ninguna regla.")

if __name__ == "__main__":
    main()
