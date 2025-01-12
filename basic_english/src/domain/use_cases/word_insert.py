from abc import ABC, abstractmethod
from typing import Dict

class WordInsert(ABC):
    @abstractmethod
    def insert(self, word: str, translation: str, formal: bool, type_word: str) -> Dict: pass