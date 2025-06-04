from interfaces.i_benefit import IBenefit
from domain.context import Context

class GenericBenefit(IBenefit):
    def __init__(self, description: str): 
        self.description = description 

    def apply(self, context: Context) -> None:        
        print(f"[BENEFIT] applying benefits: {self.description}")