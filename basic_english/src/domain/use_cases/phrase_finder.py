from abc import ABC, abstractmethod
from typing import Dict, List

class PhraseFinder(ABC):
    @abstractmethod
    def find(self, phrase: str) -> Dict: pass

    @abstractmethod
    def find_all(self) -> Dict: pass