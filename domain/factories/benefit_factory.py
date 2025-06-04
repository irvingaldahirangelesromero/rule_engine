from interfaces.i_benefit import IBenefit
from domain.generic_benefit import GenericBenefit

class BenefitFactory:
    @staticmethod
    def dict_to_benefit(data: dict)-> IBenefit:
        return GenericBenefit(data["description"])