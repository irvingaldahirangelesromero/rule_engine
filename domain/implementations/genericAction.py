# domain/actions/generic_action.py
from venv import logger
from interfaces.i_actions import IAction
from domain.context import Context
import logging

class GenericAction(IAction):
    #     Acción genérica que, al ejecutarse, dispara un proceso (p. ej. enviar correo). Por ahora solo imprime para depuración.
    
    def __init__(self, type_: str, params: dict):
        self.type = type_ # nombre de la acción (por ejemplo, 'aplicar_descuento')
        self.params = params # parámetros específicos para esa acción (por ejemplo, porcentaje de descuento, email, etc.)

    def run_action(self, context: Context) -> None:
        # En entorno real, delegar a un servicio de infraestructura (EmailService, etc.)
        logger.info(f"[ACTION] Executing action of kind: {self.type} with the params: {self.params}")

    @classmethod
    def from_dict(cls, data: dict) -> "GenericAction":
        return cls(
            type_=data["type"],
            # Quita la clave "type" para construir los parámetros restantes
            params={k: v for k, v in data.items() if k != "type"}
        )
