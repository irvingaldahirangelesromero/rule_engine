from interfaces.i_benefit import IBenefit
from domain.context import Context

class GenericBenefit(IBenefit):
    # Beneficio genérico que, al aplicarse, realiza un efecto en el Context (por ejemplo, modificar precio, agregar bono, etc.). Por ahora solo imprime.

    def __init__(self, description: str): 
        self.description = description # texto descriptivo del beneficio (p. ej. "10% descuento")

    def apply(self, context: Context) -> None:
        # En producción, esta clase debería delegar a un servicio real,
        # p. ej. DiscountService.apply_discount(context, self.description)
        
        print(f"[BENEFIT] Aplicando beneficio: {self.description}")

    @classmethod
    def from_dict(cls, data: dict) -> "GenericBenefit":
        return cls(description=data["description"])
