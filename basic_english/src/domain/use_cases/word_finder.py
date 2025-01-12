from abc import ABC, abstractmethod
from typing import Dict

class WordFinder(ABC):
    @abstractmethod
    def find(self, word: str) -> Dict: pass
    @abstractmethod
    def find_all(self) -> Dict: pass
    @abstractmethod
    def find_all_type_word(self, type_word: str) -> Dict: pass