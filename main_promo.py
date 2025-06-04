from infrastructure.repositories.file_promos_repository import FilePromoRepository
from application.promo_evaluation_service import PromoEvaluationService
from domain.context import Context

def main():
    promos_repo = FilePromoRepository("promos.json")  
    promo_service = PromoEvaluationService(promos_repo)

    data_context = {
    "segmento": "Bodas Directas",
    "mercado": "USA",
    "propiedad": "Moon Palace Cancún",
    "habitaciones": 15,
    "noches": 4,
    "edad": 30,
    "tarifa": "PUBLIC",
    "categoria_habitacion": "deluxe",
    "es_reserva_nueva": True,
    "canal_reserva": "Contrato",
    "viajan_adultos": True,
    "fecha_reserva": "2023-06-15",
    "fecha_checkin": "2023-11-20",
    "nivel_autorizacion": "N1",
    "valida_bw_tw": True,
    "solicita_honrar_promo_pasada": False
    }

    con = Context("20USDxNoche", data_context)

    # aplicable_promos = promo_service.evaluate_all(con)
    aplicable_promos = promo_service.evaluate_by_code(con)

    if aplicable_promos:
        print("The following promotions apply:")
        for promo in aplicable_promos:
            print(f"  - {promo.get_codigo()}")
    else:
        print("No promotion applies to this context")
        
if __name__ == "__main__":
    main()