from infrastructure.repositories.file_promos_repository import FilePromoRepository
from application.promo_evaluation_service import PromoEvaluationService
from domain.context import Context

def main():
    promos_repo = FilePromoRepository("promos.json")  
    promo_service = PromoEvaluationService(promos_repo)

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

    # 4) Evaluar promociones
    aplicable_promos = promo_service.evaluate_all(con)

    # 5) Mostrar resultados
    if aplicable_promos:
        print("Las siguientes PROMOCIONES aplican:")
        for promo in aplicable_promos:
            print(f"  - {promo.get_codigo()}")
    else:
        print("Ninguna promoción aplica para este contexto.")

if __name__ == "__main__":
    main()