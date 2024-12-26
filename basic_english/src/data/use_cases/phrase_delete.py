from typing import Dict, List
from basic_english.src.domain.use_cases.phrase_delete import PhraseDelete as PhraseDeleteInterface
from ..interfaces.phrases_repository import PhrasesRepositoryInterface
from basic_english.src.domain.models.phrases import Phrases

class PhraseDelete(PhraseDeleteInterface):
    def __init__(self, phrases_repository: PhrasesRepositoryInterface) -> None:
        self.__phrases_repository = phrases_repository

    def delete(self, phrase: str = None) -> Dict:
        self.__verification_delete(phrase)
        self.__phrases_repository.delete_phrase(phrase)

        return self.__format_response(phrase)

    
    @classmethod
    def __verification_delete(cls, phrases: list) -> None:
        if phrases == " " and phrases == None:
            raise Exception("Database is empty.")

    @classmethod
    def __format_response(cls, phrases: List[Phrases]) -> str:
        return f"Phrase: {phrases} deleted with success."