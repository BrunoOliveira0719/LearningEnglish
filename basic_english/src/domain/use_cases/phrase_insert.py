from abc import ABC, abstractmethod
from typing import Dict

class PhraseInsert(ABC):
    @abstractmethod
    def insert(self, phrase: str, translation: str, formal: bool) -> Dict: pass