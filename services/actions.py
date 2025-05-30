
from abc import ABC, abstractmethod

from domain.context import context

class action(ABC):

@abstractmethod
def run_action(name_action: str, context: context) -> None:
    pass
    
