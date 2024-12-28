from abc import ABC, abstractmethod
from typing import Dict

class PhraseUpdate(ABC):
    @abstractmethod
    def update(self, phrase_corrent: str, phrase: str, translation: str, formal: bool, type_phrase: str) -> Dict: pass