from abc import ABC, abstractmethod
from typing import Dict

class WordUpdate(ABC):
    @abstractmethod
    def update(self, word_corrent: str, word: str, translation: str, formal: bool, type_word: str) -> Dict: pass