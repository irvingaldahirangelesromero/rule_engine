from interfaces.i_actions import IAction
from domain.generic_action import GenericAction

class ActionFactory:
    @staticmethod
    def dict_to_action(data: dict)-> IAction:    
        type_value = data["type"]
        params = {}

        for key, value in data.items():
            if key != type:
                params[key] = value  # construye un nuevo diccionario con todos los pares excepto aquel cuya clave sea "type
        
        return GenericAction(type_value,params)