from abc import ABC, abstractmethod
from typing import Dict

class WordDelete(ABC):
    @abstractmethod
    def delete(self, word: str) -> Dict: pass