from abc import ABC, abstractmethod
from typing import Dict

class PhraseDelete(ABC):
    @abstractmethod
    def delete(self, phrase: str) -> Dict: pass