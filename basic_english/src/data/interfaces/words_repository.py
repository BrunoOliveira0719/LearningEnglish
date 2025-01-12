from abc import ABC, abstractmethod
from typing import List
from basic_english.src.domain.models.words import Words

class WordsRepositoryInterface(ABC):
    @abstractmethod
    def insert_word(self, word: str, translation: str, formal: bool, type_word: str) -> None: pass
    @abstractmethod
    def read_specific_word(self, word: str) -> List[Words]: pass
    @abstractmethod        
    def read_all_words(self) -> List[Words]: pass
    @abstractmethod        
    def read_all_type_words(self, type_word: str) -> List[Words]: pass
    @abstractmethod
    def update_word(self, word_corrent: str, json: dict) -> None: pass
    @abstractmethod
    def delete_word(self, word: str) -> None: pass
