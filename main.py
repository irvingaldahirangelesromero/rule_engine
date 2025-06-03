from os import name
from typing import Self
from infrastructure.repositories.file_rules_repository import FileRulesRepository
from application.rule_evaluation_service import RuleEvaluationService
from domain.context import Context

def main():
    rules_repo = FileRulesRepository("promos.json")  
    rule_service = RuleEvaluationService(rules_repo)

    data_context = {
      "habitaciones": 50,
      "noches": 3,
      "segmento": "Bodas Directas",
      "mercado": "México",
      "edad": 16,
      "adultos_por_habitacion": 2,
      "canal_reserva": "Contrato",
      "tarifa": "Normal",
      "propiedad": "Moon Palace Cancún",
      "fecha_checkin": "2025-07-15",
      "fecha_reserva": "2025-06-01",
      "reserva": "nueva",
      "BW_TW": True
    }

    con = Context("20 USD", data_context)

    rules_applied = rule_service.evaluate_all(con)

    if rules_applied:
        print("the following rules were applied:")
        for rule in rules_applied:
            print(f"- {rule}")
    else:
        print("no rule was applied")

if __name__ == "__main__":
    main()