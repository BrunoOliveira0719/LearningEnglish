from abc import ABC, abstractmethod
from typing import Dict

class PhraseFinder(ABC):
    @abstractmethod
    def find(self, phrase: str) -> Dict: pass
    @abstractmethod
    def find_all(self) -> Dict: pass
    @abstractmethod
    def find_all_type_phrase(self, type_phrase: str) -> Dict: pass