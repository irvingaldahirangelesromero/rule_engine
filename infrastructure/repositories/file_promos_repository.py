import json
from typing import List
from interfaces.i_promo import IPromo
from interfaces.i_promo_file import IPromosFile
from domain.promo import Promo 

class FilePromoRepository(IPromosFile):
    def __init__(self, path_file:str):
        self.path_file = path_file # Ruta de promos

    def load_promos(self) -> List[IPromo]:
        try:
            with open(self.path_file, 'r', encoding='utf8') as file: # 'r': modo de apertura del archivo 
                data = json.load(file)
        except Exception as e:
            raise

        promos: List[IPromo] = []
        for p in data.get("promotions", []): 
            promo = Promo.dict_to_promo(p) 
            promos.append(promo)

        return promos
    
    def get_by_code(self, code: str) -> IPromo | None:
        code = code.strip().lower()
        for promo in self.load_promos():
            if promo.get_codigo().strip().lower() == code:
                return promo
        return None