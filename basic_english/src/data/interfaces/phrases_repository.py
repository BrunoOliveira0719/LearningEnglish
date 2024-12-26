from abc import ABC, abstractmethod
from typing import List
from basic_english.src.domain.models.phrases import Phrases

class PhrasesRepositoryInterface(ABC):
    @abstractmethod
    def insert_phrase(self, phrase: str, translation: str, formal: bool) -> None: pass
    @abstractmethod
    def read_specific_phrase(self, phrase: str) -> List[Phrases]: pass
    @abstractmethod        
    def read_all_phrases(self) -> List[Phrases]: pass
    @abstractmethod
    def update_phrase(self, phrase_corrent: str, json: dict) -> None: pass
    @abstractmethod
    def delete_phrase(self, phrase: str) -> None: pass
