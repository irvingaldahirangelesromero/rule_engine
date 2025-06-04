from interfaces.i_criterion import ICriterion
from domain.generic_criterion import GenericCriterion

class CriterionFactory:
    @staticmethod
    def dict_to_criterion(data: dict)-> ICriterion:
        field = data["field"]
        operator = data["operator"]
        value = data["value"]
    
        return GenericCriterion(field,operator,value)